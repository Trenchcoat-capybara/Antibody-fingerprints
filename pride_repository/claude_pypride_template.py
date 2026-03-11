import requests
import csv
import time
import json

BASE_URL = "https://www.ebi.ac.uk/pride/ws/archive/v2"
SEARCH_URL = f"{BASE_URL}/search/projects"

# -- Extend any list freely to broaden or narrow your search ----

SAMPLE_TERMS = [
        "serum",
        "plasma",
        ]

DISEASE_TERMS = [
        "allergy",
        "allergic",
        "allergen",
        "atopy",
        "atopic",
        "IgE",
        "asthma",
        "rhinitis",
        "hypersensitivity",
        "anaphylaxis",
        "urticaria",
        "eczema",
        "sensitization",
        "sensitisation",
        ]

EXCLUSION_TERMS = [
        "mouse",
        "murine",
        "rat",
        "bovine",
        "plant",
        "pollen extract",
        "cell line",
        "in vitro",
        ]


SEARCH_FIELDS = [
        "title", "projectDescription", "sampleProcessingProtocol",
        "dataProcessingProtocol", "keywords", "diseases", 
        "organisms", "ogranismsPart", "tissues", "projectTags"
        ]

# ----------------------------------------------------------------------------------------

def get_metadata_text(project: dict) -> str:
    """Concatenate all searchable metadata fields into a single lowercase string."""
    text_parts = []
    for field in SEARCH_FIELDS:
        val = project.get(field, "")
        if isinstance(val, list):
            text_parts.extend([str(v) for v in val])
        elif val:
            text_parts.append(str(val))
    return " ".join(text_parts).lower()

def passes_inclusion_filter(text: str, sample_term: str, disease_term:str) -> bool:
    """Both the sample term and disease term must appear in the metadata."""
    return sample_term.lower() in text and disease_term.lower() in text

def get_exclusion_match(text: str) -> str | None:
    """Return the first exclusion term found in the text, or None if clean."""
    for term in EXCLUSION_TERMS:
        if term.lower() in text:
            return term
    return None

def search_pride(keyword: str, page_size: int = 100) -> list[dict]:
    """Fetch all pages for a given combined keyword string."""
    results = []
    page = 0
    while True:
        params = {
                "keyword":          keyword,
                "pageSize":         page_size,
                "page":             page,
                "sortDirection":    "DESC",
                "sortFields":       "submissionDate",
                }
        try:
            resp = requests.get(SEARCH_URL, params = params, timeout = 30)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            print(f" [ERROR] keyword = '{keyword}', page = {page}: {e}")
            break

        if isinstance(data, list):
            projects = data
        elif "_embedded" in data:
            projects = data["_embedded"].get("compactprojects", [])
        else:
            projects = data.get("content", [])

        if not projects:
            break
        results.extend(projects)
        print(f"page {page}: {len(projects)} results")
        if len(projects) < page_size:
            break
        page += 1
        time.sleep(0.3)
    return results

def deduplicate(projects: list[dict]) -> list[dict]:
    seen = {}
    for p in projects:
        acc = p.get("accession", "")
        if acc and acc not in seen:
            seen[acc] = p
    return list(seen.values())

def extract_row(p: dict, flagged_reason: str = "") -> dict:
    def listify(val):
        if isinstance(val, list):
            return "; ".join(str(v) for v in val)
        return str(val) if val else ""

    row = {
        "accession":        p.get("accession", ""),
        "title":            p.get("title", ""),
        "description":      p.get("projectDescription", ""),
        "submission_date":  p.get("submissionDate", ""),
        "publication_date": p.get("publicationDate", ""),
        "keywords":         listify(p.get("keywords", [])),
        "diseases":         listify(p.get("diseases", [])),
        "organisms":        listify(p.get("organisms", [])),
        "organisms_part":   listify(p.get("organismsPart", [])),
        "tissues":          listify(p.get("tissues", [])),
        "instruments":      listify(p.get("instruments", [])),
        "pubmed_ids":       listify(p.get("references", [])),
        "pride_url":        f"https://www.ebi.ac.uk/pride/archive/projects/{p.get('accession', '')}",
            }
    if flagged_reason:
        row["flagged_reason"] = flagged_reason
    return row

def write_csv(rows: list[dict], filename: str):
    if not rows:
        print(f" (no rows to write for '{filename}')")
        return
    with open(filename, "w", newline = "", encoding = "utf-8") as f:
        writer = csv.DictWriter(f, fieldnames = rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} datasets to '{filename}'") 

def main():
    n_queries = len(SAMPLE_TERMS) * len(DISEASE_TERMS)
    print(f"=== PRIDE Dataset Search ===")
    print(F"Running {len(SAMPLE_TERMS)} x {len(DISEASE_TERMS)} = {n_queries} query combinations")
    print(f"Exclusion terms: {EXCLUSION_TERMS}\n")

    all_projects = []

    for sample_term in SAMPLE_TERMS:
        for disease_term in DISEASE_TERMS:
            combined = f"{sample_term} {disease_term}"
            print(f"QUerying: '{combined}'")
            results = search_pride(combined)
            passing = [p for p in results
                       if passes_inclusion_filter(get_metadata_text(p), sample_term, disease_term)]
            print(f" -> {len(results)} raw results, {len(passing)} passed inclusion filter")
            all_projects.extend(passing)

    print(f"\nTotal before dedup: {len(all_projects)}")
    unique = deduplicate(all_projects)
    print(f"After deduplication: {len(unique)}")

    # Split into confirmed and flagged
    confirmed = []
    flagged = []

    for p in unique:
        text = get_metadata_text(p)
        exclusion_match = get_exclusion_match(text)
        if exclusion_match:
            flagged.append((p, exclusion_match))
        else:
            confirmed.append(p)

    confirmed.sort(key = lambda x: x.get("submissionDate", ""), reverse = True)
    flagged.sort(key = lambda x: x[0].get("submissionDate", ""), reverse = True)

    # Console summary
    print(f"\n=== Confirmed results: {len(confirmed)} ===")
    for p in confirmed:
        print(f" {p.get('accession', '?')} - {p.get('title', '(no title)')}")
        print(f" Submitted: {p.get('submissionDate', '?')} | Sample: {p.get('organismsPart', '?')}")

    print(f"\n=== Flagged results (exclusion terms matched): {len(flagged)} ===")
    for p, reason in flagged:
        print(f" {p.get('accession', '?')} - {p.get('title', '(no title)')}")
        print(f" Flagged for: '{reason}'")

    # Write outputs
    print("\n=== Writing output files ==")
    write_csv([extract_row(p) for p in confirmed],
              "pride_disease_serum_results.csv")
    write_csv([extract_row(p, reason) for p, reson in flagged],
              "pride_disease_serum_flagged.csv")

    with open("pride_disease_serum_raw.json", "w", encoding = "utf-8") as f:
        json.dump(confirmed, f, indent = 2)
    print(f" Full JSON saved to 'pride_disease_serum_raw")




if __name__ == "__main__":
    main()
