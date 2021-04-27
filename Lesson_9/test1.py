import argparse
import csv
from pprint import pprint

parser = argparse.ArgumentParser(description="find_a_car")
parser.add_argument('--year', default=None, nargs='?')
parser.add_argument('--brand', default=None, nargs='?')
parser.add_argument('--color', default=None, nargs='?')
parser.add_argument('--fuel', default=None, nargs='?')
args = parser.parse_args()
argsdict = vars(args)

brand = argsdict['brand']
color = argsdict['color']
year = argsdict['year']
fuel = argsdict['fuel']
x = 0
finlist = list()


def makelist():
    with open('C:\\tr1\\tz_opendata_z01012021_po01042021.csv', "r", encoding='utf-8') as f1:
        finlist.append(['D_REG BRAND MODEL COLOR MAKE_YEAR FUEL NEW_REG_NEW'])
        csv_reader = csv.reader(f1, delimiter=';')
        for row in csv_reader:
            global x
            if brand in row or brand == None:
                if color in row or color == None:
                    if fuel in row or fuel == None:
                        if year in row or year == None:
                            endlist = list()
                            if len(row[18]) != "":
                                endlist.append([row[4], row[7], row[10], row[9], row[14], row[18]])
                                finlist.append(*endlist)
                                x += 1
                            else:
                                endlist.append([row[4], row[7], row[10], row[9], row[14]])
                                finlist.append(*endlist)
                                x += 1
        print(x)


def makefile():
    with open('C:\\tr1\\newfile.csv', "w", encoding='utf-8') as f2:
        csv_writer = csv.writer(f2)
        csv_writer.writerows(finlist)


makelist()
makefile()
with open('C:\\tr1\\newfile.csv', "r", encoding='utf-8') as f3:
    csv_reader2 = csv.reader(f3)
    print(type(csv_reader2))
    for i in csv_reader2:
        print(i)

# print(x)
pprint(finlist)
