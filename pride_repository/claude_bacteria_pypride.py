"""
Search PRIDE Archive for serum datasets from allergy patients.
Uses the PRIDE REST API v2 with AND logic via a nested loop over two term lists.

Requirements:
    pip install requests

Usage:
    python search_pride_allergy_serum.py

Output:
    - pride_allergy_serum_results.csv
    - pride_allergy_serum_raw.json
"""

import requests
import csv
import time
import json

# Correct base URL and search endpoint (confirmed from PRIDE API docs)
BASE_URL   = "https://www.ebi.ac.uk/pride/ws/archive/v2"
SEARCH_URL = f"{BASE_URL}/search/projects"

# ── Extend either list freely to broaden or narrow your search ────────────────

SAMPLE_TERMS = [
    "serum",
    "plasma",
    "infection",
]

DISEASE_TERMS = [
    "Coli",
    "bacteria",
    "staph",
    "tuberculosis",
    "strept",
    "wound",
    "infection",
]

# ─────────────────────────────────────────────────────────────────────────────

def passes_post_filter(project: dict, sample_term: str, disease_term: str) -> bool:
    """Confirm both terms appear somewhere in the project's full metadata text."""
    text_parts = []
    for field in ["title", "projectDescription", "sampleProcessingProtocol",
                  "dataProcessingProtocol", "keywords", "diseases",
                  "organisms", "organismsPart", "tissues", "projectTags"]:
        val = project.get(field, "")
        if isinstance(val, list):
            text_parts.extend([str(v) for v in val])
        elif val:
            text_parts.append(str(val))

    full_text = " ".join(text_parts).lower()
    return sample_term.lower() in full_text and disease_term.lower() in full_text


def search_pride(keyword: str, page_size: int = 100) -> list[dict]:
    """Fetch all pages for a given combined keyword string."""
    results = []
    page = 0
    while True:
        params = {
            "keyword":       keyword,
            "pageSize":      page_size,
            "page":          page,
            "sortDirection": "DESC",
            "sortFields":    "submissionDate",
        }
        try:
            resp = requests.get(SEARCH_URL, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            print(f"  [ERROR] keyword='{keyword}', page={page}: {e}")
            break

        # Handle both response shapes the API may return
        if isinstance(data, list):
            projects = data
        elif "_embedded" in data:
            projects = data["_embedded"].get("compactprojects", [])
        else:
            projects = data.get("content", [])

        if not projects:
            break
        results.extend(projects)
        print(f"    page {page}: {len(projects)} results")
        if len(projects) < page_size:
            break
        page += 1
        time.sleep(0.3)  # be polite to the API
    return results


def deduplicate(projects: list[dict]) -> list[dict]:
    seen = {}
    for p in projects:
        acc = p.get("accession", "")
        if acc and acc not in seen:
            seen[acc] = p
    return list(seen.values())


def extract_row(p: dict) -> dict:
    def listify(val):
        if isinstance(val, list):
            return "; ".join(str(v) for v in val)
        return str(val) if val else ""

    return {
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


def main():
    n_queries = len(SAMPLE_TERMS) * len(DISEASE_TERMS)
    print(f"=== PRIDE Serum + Allergy Dataset Search ===")
    print(f"Endpoint: {SEARCH_URL}")
    print(f"Running {len(SAMPLE_TERMS)} x {len(DISEASE_TERMS)} = {n_queries} query combinations\n")

    all_projects = []

    for sample_term in SAMPLE_TERMS:
        for disease_term in DISEASE_TERMS:
            combined = f"{sample_term} {disease_term}"
            print(f"Querying: '{combined}'")
            results = search_pride(combined)
            passing = [p for p in results if passes_post_filter(p, sample_term, disease_term)]
            print(f"  → {len(results)} raw results, {len(passing)} passed post-filter")
            all_projects.extend(passing)

    print(f"\nTotal before dedup: {len(all_projects)}")
    unique = deduplicate(all_projects)
    print(f"After deduplication: {len(unique)}")

    unique.sort(key=lambda x: x.get("submissionDate", ""), reverse=True)

    # Console summary
    print("\n=== Results ===")
    for p in unique:
        print(f"\n  {p.get('accession','?')} — {p.get('title','(no title)')}")
        print(f"  Submitted: {p.get('submissionDate','?')}  |  Diseases: {p.get('diseases','?')}")
        print(f"  Sample: {p.get('organismsPart','?')}")
        print(f"  URL: https://www.ebi.ac.uk/pride/archive/projects/{p.get('accession','')}")

    # Save CSV
    rows = [extract_row(p) for p in unique]
    if rows:
        csv_file = "pride_allergy_serum_results.csv"
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nSaved {len(rows)} datasets to '{csv_file}'")
    else:
        print("\nNo results found — try relaxing the term lists.")

    # Save full JSON
    json_file = "pride_allergy_serum_raw.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(unique, f, indent=2)
    print(f"Full JSON saved to '{json_file}'")


if __name__ == "__main__":
    main()
