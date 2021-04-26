import csv

m = 'MAZDA'
x = 0
c = None
y = '02.03.2021'
f = 'БЕНЗИН'
with open('C:\\tr1\\tz_opendata_z01012021_po01042021.csv', "r", encoding='utf-8') as f1:
    csv_reader = csv.reader(f1, delimiter=';')
    for row in csv_reader:
        if m in row or m == None:
            if c in row or c == None:
                if f in row or f == None:
                    if y in row or y == None:
                        print(row)
                        x += 1

    print(x)
