import argparse
import csv
import re

def check_iata():
    if iata_code:
        if iata_code != re.match(r"\w{3}", iata_code)[0].upper():
            raise ValueError("incorrect iata_code")
    return iata_code

def check_args():
    argslist = []
    for arg in (check_iata(), country, name):
        if arg:
            argslist.append(arg)
    if len(argslist) > 1:
        raise ValueError("MultipleOptionsError")
    if len(argslist) < 1:
        raise ValueError("NoOptionsFoundError")
    return argslist


def find_match():
    with open(datafile, "r", encoding='utf-8') as file1:
        reader = csv.DictReader(file1)
        for line in reader:
            for str in line.values():
                if str.find(check_args()[0]) >= 0:
                    print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="find_corona")
    parser.add_argument('--iata_code', default=None, nargs='?')
    parser.add_argument('--country', default=None, nargs='?')
    parser.add_argument('--name', default=None, nargs='?')
    argsdict = vars(parser.parse_args())
    datafile = str('C:\\tr1\\airport-codes_csv.csv')
    iata_code = argsdict['iata_code']
    country = argsdict['country']
    name = argsdict['name']

    find_match()
