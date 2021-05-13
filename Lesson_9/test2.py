import argparse
import csv


def make_list():
    datafile = str('C:\\tr1\\' + argsdict['o'])
    reg_num = argsdict['reg_num']
    with open(datafile, "r", encoding='utf-8') as f1:
        csv_reader = csv.reader(f1, delimiter=';')
        for row in csv_reader:
            if all(var in row for var in varlist):
                templist = []
                if reg_num is True and row[-1] != "":
                    templist.append([row[4], row[7], row[8], row[10], row[9], row[14], row[18]])
                    finlist.append(*templist)
                elif reg_num is False:
                    templist.append([row[4], row[7], row[8], row[10], row[9], row[14], row[18]])
                    finlist.append(*templist)


def make_name():
    filename = 'C:\\tr1\\'
    templist = []
    for var in varlist:
        templist.append(var)
    filename = filename + '-'.join(templist)+".csv"
    return filename


def make_file():
    with open(make_name(), "w", encoding='utf-8') as f2:
        csv_writer = csv.writer(f2)
        csv_writer.writerow(['D_REG', 'BRAND', 'MODEL', 'COLOR', 'MAKE_YEAR', 'FUEL', 'NEW_REG_NEW'])
        csv_writer.writerows(finlist)


def clean_vars():
    for var in varlist:
        if var is None:
            varlist.remove(var)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="find_a_car")
    parser.add_argument('--o')
    parser.add_argument('--year', default=None, nargs='?')
    parser.add_argument('--brand', default=None, nargs='?')
    parser.add_argument('--color', default=None, nargs='?')
    parser.add_argument('--fuel', default=None, nargs='?')
    parser.add_argument('--reg_num', action='store_true')
    args = parser.parse_args()
    argsdict = vars(args)
    varlist = [argsdict['brand'], argsdict['year'], argsdict['color'], argsdict['fuel']]
    finlist = []
    if all(var is None for var in varlist):
        print("Please enter parameters")
    else:
        clean_vars()
        make_list()
        make_name()
        make_file()
