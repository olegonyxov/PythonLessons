import argparse
import csv


def make_file():
    datafile = str('C:\\tr1\\' + argsdict['o'])
    reg_num = argsdict['reg_num']
    with open(datafile, "r", encoding='utf-8') as f1:
        csv_reader = csv.DictReader(f1, delimiter=';')
        with open(make_name(), "w", encoding='utf-8') as f2:
            csv_writer = csv.DictWriter(f2, fieldnames=fieldnames, delimiter='|')
            csv_writer.writeheader()
            for row in csv_reader:
                if all(var in row.values() for var in clean_vars()):
                    if row['N_REG_NEW'] != "" and reg_num:
                        findict.update(
                            {'D_REG': row['D_REG'], 'BRAND': row['BRAND'], 'MODEL': row['MODEL'], 'COLOR': row['COLOR'],
                             'MAKE_YEAR': row['MAKE_YEAR'], 'FUEL': row['FUEL'], 'N_REG_NEW': row['N_REG_NEW']})
                        csv_writer.writerows([findict])
                    elif not reg_num:
                        findict.update({
                            'D_REG': row['D_REG'], 'BRAND': row['BRAND'], 'MODEL': row['MODEL'], 'COLOR': row['COLOR'],
                            'MAKE_YEAR': row['MAKE_YEAR'], 'FUEL': row['FUEL']})
                        csv_writer.writerows([findict])


def make_name():
    filename = 'C:\\tr1\\'
    templist = []
    for var in clean_vars():
        templist.append(var.lower())
    filename = filename + '-'.join(templist) + ".csv"
    return filename


def clean_vars():  # работает при -273 с одним аргументом
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
    args = parser.parse_args()
    argsdict = vars(args)
    fieldnames = ('D_REG', 'BRAND', 'MODEL', 'COLOR', 'MAKE_YEAR', 'FUEL', 'N_REG_NEW')
    varlist = [argsdict['brand'], argsdict['year'], argsdict['color'], argsdict['fuel']]
    findict = {}
    if all(var is None for var in varlist):
        print("Please enter parameters")
    else:
        make_file()
