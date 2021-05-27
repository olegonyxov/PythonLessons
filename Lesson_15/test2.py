import csv
datafile = 'C:\\tr1\\airport-codes_csv.csv'
with open(datafile, "r", encoding='utf-8') as file1:
    reader = csv.DictReader(file1)
    for line in reader:
        print(line)