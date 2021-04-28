import argparse
import csv

parser = argparse.ArgumentParser(description="find_a_car")
parser.add_argument('--o')
parser.add_argument('--year', default=None, nargs='?')
parser.add_argument('--brand', default=None, nargs='?')
parser.add_argument('--color', default=None, nargs='?')
parser.add_argument('--fuel', default=None, nargs='?')
parser.add_argument('--reg_num', action='store_true')
args = parser.parse_args()
argsdict = vars(args)
datafile = str('C:\\tr1\\' + argsdict['o'])
brand = argsdict['brand']
color = argsdict['color']
year = argsdict['year']
fuel = argsdict['fuel']
reg_num = argsdict['reg_num']
varlist = [brand, year, color, fuel]
finlist = list()


def make_list():
    with open(datafile, "r", encoding='utf-8') as f1:
        csv_reader = csv.reader(f1, delimiter=';')
        for row in csv_reader:
            if brand in row or brand == None:
                if color in row or color == None:
                    if fuel in row or fuel == None:
                        if year in row or year == None:
                            templist = list()
                            if reg_num == True and row[-1] != "":
                                templist.append([row[4], row[7], row[8], row[10], row[9], row[14], row[18]])
                                finlist.append(*templist)

                            elif reg_num == False:
                                templist.append([row[4], row[7], row[8], row[10], row[9], row[14], row[18]])
                                finlist.append(*templist)


def make_name():
    filename = 'C:\\tr1\\'
    templist = list()
    for var in varlist:
        if var != None:
            templist.append(var)
    filename = filename + '-'.join(templist)
    return filename


def make_file():
    with open(make_name(), "w", encoding='utf-8') as f2:
        csv_writer = csv.writer(f2)
        csv_writer.writerow(['D_REG', 'BRAND', 'MODEL', 'COLOR', 'MAKEYEAR', 'FUEL', 'NEW_REG_NEW'])
        csv_writer.writerows(finlist)


def readfile():
    with open(make_name(), "r", encoding='utf-8') as f3:
        csv_reader2 = csv.DictReader(f3)
        for i in csv_reader2:
            print(i)


if __name__ == '__main__':
    if brand == None and color == None and year == None and fuel == None:
        print("Please enter parameters")
    else:
        make_list()
        make_name()
        make_file()
        readfile()
