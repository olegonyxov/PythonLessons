import argparse
import csv


def make_file():
    datafile = str('C:\\tr1\\' + argsdict['o'])
    reg_num = argsdict['reg_num']
    findict = {}
    with open(datafile, "r", encoding='utf-8') as f1:
        with open(make_name(), "w", encoding='utf-8') as f2:
            csv_reader = csv.DictReader(f1, delimiter=';')
            csv_writer = csv.DictWriter(f2, fieldnames=fieldnames, delimiter='|')
            csv_writer.writeheader()
            for row in csv_reader:
                if all(var in row.values() for var in  # c учетом логики применения, чем условия
                       clean_vars()):
                    findict.update(
                        {'D_REG': row['D_REG'], 'BRAND': row['BRAND'], 'MODEL': row['MODEL'], 'COLOR': row['COLOR'],
                         'MAKE_YEAR': row['MAKE_YEAR'], 'FUEL': row['FUEL']})
                    if row['N_REG_NEW'] != "" and reg_num:
                        findict.update(
                            {'NEW_REG_NEW': row['N_REG_NEW']})
                    csv_writer.writerows([findict])


def make_name():
    filename = 'C:\\tr1\\'
    templist = []
    for var in clean_vars():
        templist.append(var.lower())
    filename = filename + '-'.join(templist) + ".csv"
    return filename


def clean_vars():  # работает при -273 с одним н.о аргументом
    newvarlist = []
    for i in range(len(varlist)):
        if varlist[i]:
            varlist[i] = varlist[i].upper()
            newvarlist.append(varlist[i])
    return newvarlist


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="find_a_car")
    parser.add_argument('--o')
    parser.add_argument('--year', default=None, nargs='?')
    parser.add_argument('--brand', default=None, nargs='?')
    parser.add_argument('--color', default=None, nargs='?')
    parser.add_argument('--fuel', default=None, nargs='?')
    parser.add_argument('--reg_num', action='store_true')
    argsdict = vars(parser.parse_args())
    fieldnames = ('D_REG', 'BRAND', 'MODEL', 'COLOR', 'MAKE_YEAR', 'FUEL', 'NEW_REG_NEW')
    varlist = [argsdict['brand'], argsdict['year'], argsdict['color'], argsdict['fuel']]
    if all(not var for var in varlist):
        print("Please enter parameters")
    else:
        make_file()
