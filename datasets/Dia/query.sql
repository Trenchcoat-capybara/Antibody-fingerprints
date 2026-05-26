-- query to get disease frame for analysis
SELECT 
  DENSE_RANK() OVER (ORDER BY "File.Name") AS patient_id,
  "Genes",
  CASE
    WHEN "File.Name" ILIKE '%ctr%' Then 'Control'
    WHEN "File.Name" ILIKE '%covid%' THEN 'Covid'
    WHEN "File.Name" ILIKE '%monkey%' THEN 'Monkey_Pox'
  END AS disease,
  CASE
    WHEN "File.Name" ILIKE '%control%' THEN 'Control'
    WHEN "File.Name" ILIKE '%Viral%' THEN 'Viral'
  END AS disease_type,
  "PG.Quantity" AS count
FROM dia
WHERE "Protein.Ids" = 'P01871'
  OR "Protein.Ids" = 'P01880'
  OR "Protein.Ids" = 'P01854'
  OR "Protein.Ids" = 'P01876'
  OR "Protein.Ids" = 'P01877'
  OR "Protein.Ids" = 'P01857'
  OR "Protein.Ids" = 'P01859'
  OR "Protein.Ids" = 'P01860'
  OR "Protein.Ids" = 'P01861';


  -- query for data 
SELECT 
  DISTINCT("Run"),
  DENSE_RANK() OVER (ORDER BY "File.Name") AS patient_id,
  CASE
    WHEN "File.Name" ILIKE '%ctr%' Then 'Control'
    WHEN "File.Name" ILIKE '%covid%' THEN 'Covid'
    WHEN "File.Name" ILIKE '%monkey%' THEN 'Monkey_Pox'
  END AS disease,
  'PXD036072' AS accension_number
FROM dia
GROUP BY "Run", "File.Name";

