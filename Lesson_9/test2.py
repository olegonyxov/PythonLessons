import argparse
import csv

parser = argparse.ArgumentParser(description="find_a_car")
parser.add_argument('--year', default=None, nargs='?')
parser.add_argument('--brand', default=None, nargs='?')
parser.add_argument('--color', default=None, nargs='?')
parser.add_argument('--fuel', default=None, nargs='?')
parser.add_argument('--reg_num', default=1, nargs='?')
args = parser.parse_args()
argsdict = vars(args)

brand = argsdict['brand']
color = argsdict['color']
year = argsdict['year']
fuel = argsdict['fuel']
reg_num = argsdict['reg_num']
varlist = [brand, color, year, fuel]
finlist = list()

def make_name():
    filename = 'C:\\tr1\\'
    tempfile=list()
    for var in varlist:
        if var !=None:
           tempfile.append(var)
    filename =filename+'-'.join(tempfile)
    print(filename)

make_name()