library(DBI)
library(RPostgres)
# patient_# <- c(patient_number, organism, category ? virus, disease, ftp)
patient_1 <- c(1, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A1_heat_DIA.wiff2.Zip')
patient_2 <- c(2, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A2_heat_DIA.wiff2.Zip')
patient_3 <- c(3, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A3_heat_DIA.wiff2.Zip')
patient_4 <- c(4, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A4_heat_DIA.wiff2.Zip')
patient_5 <- c(5, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A5_heat_DIA.wiff2.Zip')
patient_6 <- c(6, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A6_heat_DIA.wiff2.Zip')
patient_7 <- c(7, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A7_heat_DIA.wiff2.Zip')
patient_8 <- c(8, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A8_heat_DIA.wiff2.Zip')
patient_9 <- c(9, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A9_heat_DIA.wiff2.Zip')
patient_10 <- c(10, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A10_heat_DIA.wiff2.Zip')
patient_11 <- c(11, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A11_heat_DIA.wiff2.Zip')
patient_12 <- c(12, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-A12_heat_DIA.wiff2.Zip')
patient_13 <- c(13, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-B1_heat_DIA.wiff2.Zip')
patient_14 <- c(14, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-B2_heat_DIA.wiff2.Zip')
patient_15 <- c(15, 'Homo Sapien', 'Control', 'None', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_Ctr-B3_heat_DIA.wiff2.Zip')

patient_16 <- c(16, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E1_heat_DIA.wiff2.Zip')
patient_17 <- c(17, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E2_heat_DIA.wiff2.Zip')
patient_18 <- c(18, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E3_heat_DIA.wiff2.Zip')
patient_19 <- c(19, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E4_heat_DIA.wiff2.Zip')
patient_20 <- c(20, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E5_heat_DIA.wiff2.Zip')
patient_21 <- c(21, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E6_heat_DIA.wiff2.Zip')
patient_22 <- c(22, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E7_heat_DIA.wiff2.Zip')
patient_23 <- c(23, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E8_heat_DIA.wiff2.Zip')
patient_24 <- c(24, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E9_heat_DIA.wiff2.Zip')
patient_25 <- c(25, 'Homo Sapien', 'Virus', 'Covid', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_COVID-E10_heat_DIA.wiff2.Zip')


patient_26 <- c(26, 'Homo Sapien', 'Virus', 'Monkey_Pox', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_MPX-D1_heat_DIA.wiff2.Zip')
patient_27 <- c(27, 'Homo Sapien', 'Virus', 'Monkey_Pox', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_MPX-D2_heat_DIA.wiff2.Zip')
patient_28 <- c(28, 'Homo Sapien', 'Virus', 'Monkey_Pox', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_MPX-D3_heat_DIA.wiff2.Zip')
patient_29 <- c(29, 'Homo Sapien', 'Virus', 'Monkey_Pox', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_MPX-D4_heat_DIA.wiff2.Zip')
patient_30 <- c(30, 'Homo Sapien', 'Virus', 'Monkey_Pox', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_MPX-D5_heat_DIA.wiff2.Zip')
patient_31 <- c(31, 'Homo Sapien', 'Virus', 'Monkey_Pox', 'https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/09/PXD036074/20220624_Z1_ZW_001_30-0066_MPX-D6_heat_DIA.wiff2.Zip')

patients <- rbind(patient_1, patient_2, patient_3, patient_4, patient_5,
                  patient_6, patient_7, patient_8, patient_9, patient_10,
                  patient_11, patient_12, patient_13, patient_14, patient_15,
                  patient_16, patient_17, patient_18, patient_19, patient_20,
                  patient_21, patient_22, patient_23, patient_24, patient_25,
                  patient_26, patient_27, patient_28, patient_29, patient_30,
                  patient_31)
names <- c('patient', 'species', 'disease_type', 'disease', 'ftp')
colnames(patients) <- names

# con = dbConnect(RPostgres::Postgres(), dbname = 'antibodies')
# dbGetQuery(con, 'SELECT * from patients limit 10')
# dbWriteTable(con, 'patients', patients)
