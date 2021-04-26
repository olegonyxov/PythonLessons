import csv

m = 'MAZDA'
c = None
y = '02.03.2021'
f = 'БЕНЗИН'
x = 0
finlist = list()

with open('C:\\tr1\\tz_opendata_z01012021_po01042021.csv', "r", encoding='utf-8') as f1:
    finlist.append('D_REG BRAND MODEL COLOR MAKE_YEAR FUEL NEW_REG_NEW')
    csv_reader = csv.reader(f1, delimiter=';')
    for row in csv_reader:
        if m in row or m == None:
            if c in row or c == None:
                if f in row or f == None:
                    if y in row or y == None:
                        endlist = list()
                        endlist.append([row[4],row[7],row[10],row[9],row[14],row[18]])
                        finlist.append(endlist)
                        x += 1

    print(x)
    print(finlist)
