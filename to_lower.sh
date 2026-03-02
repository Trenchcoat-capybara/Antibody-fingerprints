#!/usr/bin/bash

file= "$1"
output= "$2"
beginning= head -n 1 $file | tr '[:upper:]' '[:lower"]' | tr ' ' '_'> $output
# add a > output file
end= tail -n +2 $file >> $output

