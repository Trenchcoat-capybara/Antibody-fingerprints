-- copy csv data to an existing table
COPY [Table_name] (Optional_columns) -- probably ascension ID
FROM '[Absolute_path]' -- '~/Documents/Bachelor project/*'
DELIMITER '[Delimiter_character]' -- '\t' for tab separated files
CSV [HEADER]; -- CSV header if the first line in csv is filled with column titles 
