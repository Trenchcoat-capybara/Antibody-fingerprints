# Disease databases from PRIDE
## in use
### Viral
- PXD036074 - Host response to Monkeypox infection (case series)  
- PXD015422 - High-resolution proteomics of Zika and Dengue serum samples
- PXD030260 - Plasma proteomic, human Ebola virus disease
    - next
### Bacterial
### Autoimmune

## Potentially useful
- PXD012412 - Proteomic analyses of Mycobacterium tuberculosis associated sputum and plasma
    - if I can figure what out the ftp files plasma represents they may be useful
    - use title to find the study
- PXD020212 - Proteomic Discovery and Validation of Diagnostic Plasma Biomarkers for Pulmonary Tuberculosis
    - come back later to figure out the naming of the files, potentially achievable
- PXD067583 - Human Lyme Neuroborreliosis LC-MS (plasma) 
    - DIA-NN
    - Article not linked in PRIDE
        - The diagnostic potential of proteomics and machine learning in lyme neuroborreliosis
    - two sample types, CSF and plasma, interested in plasma
        - 95 plasma with LNB (n = 27)
        - viral meningitis (n = 20)
        - control (n = 48)
## can't use
- PXD005022 - Quantitative proteomics of bloodstream infection
    - forgot to lable which dataset belongs to which patient, control or infected
- PXD005234 - In vivo and in vitro proteome analysis of HIV-1 infected, human CD4+ T cells
    - proteome of CD4+ cells, not plasma
- PXD005267 - Quantitative Proteomics analysis of Plasmodium vivax induced alterations in human serum during the acute and convalescent phases of infection
    - IgG removed
- PXD005777 - Quantitative proteome analysis of plasma microparticles for characterization of HCV-induced hepatic cirrhosis and hepatocellular carcinoma
    - 20 most abundant precursors were measured, I doubt 9 of those were antibodies
- PXD009029 - Application of Multiplexed Ion Mobility Spectrometry towards the Identification of Host Protein Signatures of Treatment Effect in Pulmonary Tuberculosis
    - 14 High abundance proteins were removed with immunoaffinity
        - See if this hits any of the antibodies, main suspect is IgG
            - Eliminates IgG, IgA and IgM
        - Done using ProteomeLab 12.7 x 79.0-mm human IgY14 LC10 affinity LC column
- PXD009112 - Defining the cellular proteolytic landscape in systemic lupus erythematosus
    - All experiments were performed in three individual replicates unless otherwise mentioned.
    - I think they forgot to lable which patient is which
        - can't find out which patient is which
- PXD009438 - Defining the cellular proteolytic landscape in systemic lupus erythematosus – nonspecific digest
    - 985 - 990 = Ctr
    - 991 - 998 = Lupus
    - Proteosomes
- PXD013548 - Rickettsia-HUVECs secretome and Rickettsia-mouse plasma proteome
    - in vitro
- PXD016843 - Characterization of plasma proteins of HIV/AIDS patients underfirst line anti-retroviral therapy
    - Used Aurum-serum protein mini kit to remove IgG
- PXD019393 - Complement deposition on Chlamydia trachomatis
    - chlamydia incubated in human serum
- PXD026906 - Proteomic analysis of serum samples of paracoccidioidomycosis patients with severe pulmonary sequel
    - ftp non existant
    - 17 patients, supposedly 1 raw file which is zipped
- PXD038929 - Systems-level temporal immune-metabolic profile in Crimean-Congo hemorrhagic fever virus infection
    - cell proteome
- PXD039509 - Human Plasma from non-Hispanic White and African American Sepsis Survivors and Non-Survivors with Primary Urinary Tract Infection LC-MS/MS
    - IgG and IgA depleted
- PXD067583 - Human Lyme Neuroborreliosis LC-MS (plasma)
    - pending
- PAD000008 - Targeted plasma proteomics reveals organ damage signatures of AIDS-related and non-communicable chronic diseases-related deaths in HIV population
    - no datasets

## Viral  
### COVID - 19    
- PXD053440 — Serum proteomics from COVID-19 patients with organ morbidities
    - Can't be used, it is recovered patients
    - fragpiped
- PXD037486 — In-depth serum proteomics of hospitalized COVID-19 patients  
    - bad notation
- PXD020601 — Serum/plasma proteomics in COVID-19 with focus on IL-6 levels  
    - atrotious notation
    - missing some of the antibodies, analysis has been performed but not sure aboutweights and other things.
- PXD024549 - Quantitative serum proteomics, immune biomarkers, disease severity
    - contains healthy, infected, and recovered patients
    - maybe tung has analysed this one already
    - may be incompatible with fragpipe
### Non-COVID  
- PXD036074 — Host response to Monkeypox infection (case series)  
    - plasma proteome, not sure if that is a serum sample
    - contains Monkeypox and covid
  
## Cancer or Tumor-related Serum proteomics  
- PXD001171 — Human serum proteomics in hepatocellular carcinoma (HCC)  
- PXD016727 — Serum glycopeptidomics & proteomics in oropharyngeal squamous cell carcinoma  
- PXD045467 — Serum proteomics in glioblastoma patients (DIA-MS)  
- PXD008583 - Serum from CRC patients, prognostic biomarker study
- (serum) PXD037541 - IgG Fc glycoform ratios in serum (via iProX)  
    - GenAI hallucination?
  
## Neurodegenerative Diseases  
- PXD011482 — Deep serum proteome profiling in Alzheimer’s diseases  
- PXD038003 - Serum/EVs, treatment response prediction
  
## Bacterial  
- PXD028437 — Proteome-wide glycosylation signatures in human plasma during infection  
    - check again with veit
    - it is a plasma sample, which is different from serum
- PXD016013 — Proteome changes after bacterial sepsis (preterm pig model)  
    - it is a plasma sample
    - pig sample not human
- PXD014522 — Species-unique peptide biomarkers of bacterial respiratory pathogens  
    - look at it latter
    - human proteins were removed
- PXD041960 — Human plasma LC-MS/MS from children with bacterial and viral infections  
    - bad documentation
    - mixing bacterial and viral infections
- PXD028437 — Plasma glycoproteomics differentiating bacterial vs viral infection   
    - not specific
    - bacterial or viral
  
## Fungal  
- PXD000642 — Quantitative proteomics of macrophage vesicles upon β-glucan (fungal component) stimulation  
    - take another look
  
## Autoimmune / Inflammatory  
- PXD020235 — Rheumatoid arthritis patient vs control serum proteomes  
  
## Parasitic  
- (serum) PXD057547 — Plasma proteomics in Loa loa (loiasis) patients  
    - plasma proteomics
    - use this one
- (serum) PXD063487 — Validation plasma proteomics in Loa loa infection  
    - appears to be a validation of PXD057547
### Helminth and nematode  



# Brute force Organism:Homo Sapien  Organism Part: Blood serum  Sort by: Accession  order by:Ascending  40/page 379 sets total
## Page 1 PAD000026 - PXD005156
- PRD000172 - Prioritization of candidate protein biomarkers from an in vitro model system of breast tumor progression toward clinical verification
- PXD000917 - Proteomic identification of anti-tetanus toxoid antibodies from human serum (HD1)
- PXD001034 - Biomarkers for Cervical Cancer. iTRAQ Discovery.
- PXD001171 - Human Serum LC-MS/MS - LC-MS/MS-based serum proteomics for identification of candidate biomarkers for hepatocellular carcinoma
- PXD001397 - PBC-DIGE - Serological comparative proteomics analysis of mitochondrial autoantibody-negative and -positive primary biliary cirrhosis
- PXD002854 - Plasma proteome profiling to assess human health and disease
- PXD003498 - Influenza A virus- integrated glycomics, proteomics and glycoproteomics
- PXD004624 - Multi-omics analysis of serum samples demonstrates reprogramming of organ functions via systemic calcium mobilization and platelet activation in metastatic melanoma patients – proteins from serum samples of melanoma patients with high tumor load
## Page 2 PXD005193 - PXD010309
- PXD005267 - Quantitative Proteomics analysis of Plasmodium vivax induced alterations in human serum during the acute and convalescent phases of infection
- PXD009007 - HIV/HCV co-infection proteomics
-- PXD009029 - Application of Multiplexed Ion Mobility Spectrometry towards the Identification of Host Protein Signatures of Treatment Effect in Pulmonary Tuberculosis
-- PXD009112 - Defining the cellular proteolytic landscape in systemic lupus erythematosus
- PXD009139 - Comparative serum proteomics of Intraductal papillary mucinous neoplasias and pacreatic adenocarcinoma
-- PXD009438 - Defining the cellular proteolytic landscape in systemic lupus erythematosus – nonspecific digest
- PXD009587 - Identification of candidate biomarkers for the early detection of radiation induced cutaneous erythema by quantitative proteomic analysis using a Data Independent Mass Spectrometry
## Page 3 PXD010328 - PXD018417
- PXD011482 - Deep undepleted human serum proteome profiling toward biomarker discovery for Alzheimer’s disease
- PXD011781 - SPIO corona - Immunoglobulin deposition on biomolecule corona determines complement opsonization efficiency of preclinical and clinical nanoparticles
- PXD014797 - Insight into the Human Pathodegradome of the V8 protease from Staphylococcus aureus
-- PXD015422 - High-resolution proteomics of Zika and Dengue serum samples

## Page 4 PXD018502 - PXD026693
- PXD018920 - Influenza A hemagglutinin glycoproteomics similarity
- PXD019008 - Discovery of biomarker candidates associated with the risk of short- and long-term relapse after infliximab withdrawal in Crohns patients: a proteomics-based study
-- PXD019393 - Complement deposition on Chlamydia trachomatis
- PXD019604 - Serum protein abundance of MDR-TB patients based on PRM analysis
- PXD025224 - Serum proteomic profiling in patients with advanced Schistosoma japonicum-induced hepatic fibrosis
- PXD025968 - Comparative analysis of serum proteins between hepatitis B virus genotype B and C infection DIA-based quantitative proteomics
## Page 5 PXD026875 - PXD031556
-- PXD026906 - Proteomic analysis of serum samples of paracoccidioidomycosis patients with severe pulmonary sequel
- PXD028429 - Proteomics of serum samples from COVID-19 ARDS and bacterial ARDS patients
- PXD028476 - Guillain-Barré syndrome following Zika virus infection is associated with a diverse spectrum of peripheral nerve reactive antibodies
## Page 6 PXD031969 - PXD039273
- PXD032734 - Serum proteomic analysis by tandem mass tags-based quantitative proteomics in pediatric obstructive sleep apnea
- PXD033989 - Serum Proteomics of Severe Fever with Thrombocytopenia Syndrome Patients
## Page 7 PXD039469 - PXD046438
- PXD040847 - Altered profile of glycosylated proteins in serum samples obtained from patients with Hashimoto′s thyroiditis following depletion of highly abundant proteins
- PXD041218 - Progresses and challenges of Strongyloides spp. proteomics
- PXD043324 - Multi-omics approach reveals serum biomarker candidates for Congenital Zika Syndrome
- PXD046237 - Benchmarking and integrating human B-cell receptor genomic and antibody proteomic profiling
## Page 8 PXD046530 - PXD054073
- PXD052579 - Serum LC-MSMS in patient of ischemic stroke
- PXD059174 - Serological paroteomic biomarkers for monitoring liver fibrosis regression in on-treatment hepatities b patients
## Page 9 PXD054347 - PXD063043
## Page 10 PXD063283 - PXD073337
-- PXD067583 - Human Lyme Neuroborreliosis LC-MS (plasma)
- PXD073337 - Longitudinal Proteomic Profiling of Bronchoalveolar Lavage Fluid (BALF) and Serum in Tuberculosis Patients


# Brute force Organism:Homo Sapien  Organism Part: Blood  Sort by: Accession  order by:Ascending  40/page 658 sets total
## Page 1 PRD000053 - PXD002798
- None
## Page 2 PXD002799 - PXD006196
-- PXD005234 - In vivo and in vitro proteome analysis of HIV-1 infected, human CD4+ T cells
## Page 3 PXD006201 - PXD010691
- PXD010519 - Plant-derived virus-like particle vaccines drive cross-presentation of influenza A hemagglutinin peptides by human monocyte-derived macrophages
## Page 4 PXD010741 - PXD014382
- PXD012958 - Proteomics pipeline for identifying variant proteins in Plasmodium falciparum parasites isolated from children presenting with malaria
- PXD013034 - Epstein-Barr Virus Induced One-Carbon Metabolism Drives B-Cell Transformation
- PXD013539 - Multi-omics analysis demonstrates unique mode of action of a potent new antimalarial compound, JPC-3210, against Plasmodium falciparum
## Page 5 PXD014425 - PXD017804
-- PXD016843 - Characterization of plasma proteins of HIV/AIDS patients underfirst line anti-retroviral therapy
## Page 6 PXD017824 - PXD021898
- PXD027241 - A new mass spectral library for high-coverage and reproducible analysis of the Plasmodium falciparum-infected red blood cell proteome
- PXD027301 - A new mass spectral library for high-coverage and reproducible analysis of the Plasmodium falciparum-infected red blood cell proteome
## Page 7 PXD021926 - PXD024197
- None
## Page 8 PXD024216 - PXD026153
- None
## Page 9 PXD026154 - PXD027334
- None
## Page 10 PXD027565 - PXD030701
- PXD029688 - identify the possible proteins that specifically bind to the 59-bp nucleotide sequence containing rs2280381
## Page 11 PXD030936 - PXD035344
- None
## Page 12 PXD035459 - PXD040572
-- PXD038929 - Systems-level temporal immune-metabolic profile in Crimean-Congo hemorrhagic fever virus infection
## Page 13 PXD040703 - PXD045161
- PXD045072 - Helicobacter pylori induces a novel form of innate immune memory via accumulation of NF-кB proteins
## Page 14 PXD045199 - PXD051740
- None
## Page 15 PXD051789 - PXD057989
- None
## Page 16 PXD058045 - PXD065519
- PXD058933 - Kinases Responding to Herpes Zoster Virus Infection Unveiled by Phosphoromics Profiling
## Page 17 PXD065732 - PXD071954
- None


# Brute force Organism:Homo Sapien  Organism Part: Blood plasma  Sort by: Accession  order by:Ascending  40/page 809 sets total
## Page 1 PAD000002 - PXD002131
-- PAD000008 - Targeted plasma proteomics reveals organ damage signatures of AIDS-related and non-communicable chronic diseases-related deaths in HIV population
-- PXD005022 - Quantitative proteomics of bloodstream infection
-- PXD005777 - Quantitative proteome analysis of plasma microparticles for characterization of HCV-induced hepatic cirrhosis and hepatocellular carcinoma
## Page 2 PXD002142 - PXD006031
- None
## Page 3 PXD006083 - PXD008945
- None
## Page 4 PXD009048 - PXD011929
- PXD010496 - Human plasma proteins detected by HPLC-MS/MS after blood incubation with E. coli treated/not treated with mucin
## Page 5 PXD012034 - PXD016428
-- PXD012412 - Proteomic analyses of Mycobacterium tuberculosis associated sputum and plasma
-- PXD013548 - Rickettsia-HUVECs secretome and Rickettsia-mouse plasma proteome
- PXD013629 - Plasma Proteome for Hepatobiliary Carcinomas
- PXD014991 - Multiplexed Quantitative Proteomics Provides Mechanistic Cues for Malaria Severity and Complexity
## Page 6 PXD016435 - PXD020354
-- PXD020212 - Proteomic Discovery and Validation of Diagnostic Plasma Biomarkers for Pulmonary Tuberculosis
## Page 7 PXD020355 - PXD023508
- None
## Page 8 PXD023521 - PXD026177
- None
## Page 9 PXD026189 - PXD028437
- PXD027997 - Systemic effects of hemorrhagic snake venom metalloproteinases: untargeted peptidomics to explore the pathodegradome of plasma proteins
- PXD028152 - Serum proteomics analysis of CCA
## Page 10 PXD028515 - PXD031338
-- PXD030260 - Plasma proteomic, human Ebola virus disease
## Page 11 PXD031458 - PXD034932
- None
## Page 12 PXD034978 - PXD038526
- None
## Page 13 PXD038528 - PXD041781
-- PXD039509 - Human Plasma from non-Hispanic White and African American Sepsis Survivors and Non-Survivors with Primary Urinary Tract Infection LC-MS/MS
## Page 14 PXD041820 - PXD045528
- PXD042003 - Human plasma LC-MS/MS from children with bacterial and viral infections
- PXD042141 - Th17 and MAIT17 cells are associated with severe Recessive Dystrophic Epidermolysis Bullosa: Staphylococcus aureus involvement
- PXD042850 - Dynamics of the blood plasma proteome during hyperacute HIV-1 infection
- PXD043815 - Pathogenesis of chikungunya virus infection associated with fatal outcome
- PXD045155 - Blood plasma from people living with HIV-1 or HIV-2
## Page 15 PXD045661 - PXD048709
- PXD046473 -  Serum antibody repertoire to influenza HA
- PXD048033 - SPATEs promote the survival of Shigella to the plasma complement system upon local hemorrhage and bacteremia
## Page 16 PXD048938 - PXD052784
- PXD051070 - Non-depleted human plasma proteome of pulmonary tuberculosis
## Page 17 PXD052798 - PXD056613
- PXD056075 - Meltome of P. falciparum across intraerythrocytic developmental cycle
## Page 18 PXD056694 - PXD060680
- PXD057692 - Proteomic analysis of plasma and duodenal tissue in patients with celiac disease: identification of potential diagnostic noninvasive biomarkers
- PXD058037 - Proteomics of Extracellular Vesicles in mild and severe dengue patients’ plasma
- PXD058381 - Typhoid toxin of Salmonella Typhi elicits host antimicrobial response during acute typhoid fever
- PXD060604 - Proteomic analysis of Plasma-derived Extracellular Vesicles reveals different biomarkers for monitoring visceral leishmaniasis progression
## Page 19 PXD060726 - PXD064059
- None
## Page 20 PXD064125 - PXD070221
- PXD064837 - Glycoproteomics analysis of Complement Factor H and its effect on complement regulatory function during Streptococcus pneumoniae-associated hemolytic uremic syndrome
- PXD068488 - Autoreactive T Cells Recognize Unique MBP Peptides Naturally Presented by EBV-Infected B Cells and Multiple Sclerosis Brain Tissue
- PXD069402 - Affinity-purification mass spectrometry on i) streptolysin O or C5a peptidase with human plasma or saliva; ii) human plasminogen with streptococcal proteins
- PXD069842 - Colonic spatial single-cell proteomics and murine models link mitochondrial dysfunction to dimeric IgA-secreting plasma cell deficiency in Crohn's disease
## Page 21 PXD070239 - PXD072647
- None
