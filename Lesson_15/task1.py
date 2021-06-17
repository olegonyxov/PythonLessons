import argparse
import csv
import re

import Exeptions1 as Ex

parser = argparse.ArgumentParser(description="search_airports")
parser.add_argument('--iata_code', default=None, nargs='?')
parser.add_argument('--country', default=None, nargs='?')
parser.add_argument('--name', default=None, nargs='?')
args = parser.parse_args()
datafile = 'C:\\tr1\\airport-codes_csv.csv'
iata_code = args.iata_code
country = args.country
name = args.name
finlist = []


def checkinput():
    inputlist = []
    if iata_code:
        inputlist.append(iata_code)
    if country:
        inputlist.append(country)
    if name:
        inputlist.append(name)
    if len(inputlist) > 1:
        raise Ex.MultipleOptionsError("Too many parameters!")
    elif len(inputlist) < 1:
        raise Ex.NoOptionsFoundError("No options found!")
    else:
        return inputlist


def check_iata():
    if iata_code:
        if iata_code != re.match(r"\w{3}", iata_code)[0].upper():
            raise Ex.IATACodeError("Wrong IATA code")
        else:
            return iata_code


def searchairport():
    with open(datafile, "r", encoding='utf-8') as file1:
        reader = csv.DictReader(file1)
        if country:
            for line in reader:
                if country == line['iso_country']:
                    finlist.append(line)
            if len(finlist) < 1:
                raise Ex.CountryNonFoundError("Country not found!")
        if iata_code:
            for line in reader:
                if iata_code == line['iata_code']:
                    finlist.append(line)
            if len(finlist) < 1:
                raise Ex.AirportNotFoundError("Airport not found!")
        if name:
            for line in reader:
                if re.search(rf"{name}", line['name']):
                    finlist.append(line)
            if len(finlist) < 1:
                raise Ex.AirportNotFoundError("Airport not found!")
    return finlist


checkinput()
check_iata()
print(searchairport())
