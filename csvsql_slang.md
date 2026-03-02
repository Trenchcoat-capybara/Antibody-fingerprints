
## Target a specific local PostgreSQL database
```
csvsql --db postgresql:///salesdb --insert customers.csv
```
insert customers.csv into database salesdb 

## Target Specific User + database
```
csvsql --db postgresql://myuser:mypassword@localhost/salesdb --insert customers.csv
```

## Target remote server
```
csvsql --db postgresql://reporter:secret@192.168.1.50:5432/analytics --insert data.csv
```

## Specify Table name
```
csvsql --db postgresql:///salesdb --insert --tables monthly_customers customers.csv
```

## Just Generate SQL (Don't Execute)
```
csvsql --dialect postgresql customers.csv
```
or
```
csvsql --dialect postgresql --tables customers customers.csv
```

## Prevent Type Guessing (Force TEXT)
```
csvsql --db postgresql:///salesdb --insert --no-inference customers.csv
```

## Large Files (Safer Approach)
```
csvsql --dialect postgresql --tables customers customers.csv > create.sql
psql salesdb -f create.sql
```

## Example converting tsv into SQL
```
csvsql -d $'\t' \
  --db postgresql:///mydb \
  --insert \
  --tables my_table \
  data.tsv
```
