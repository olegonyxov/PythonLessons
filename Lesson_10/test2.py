import csv
from pprint import pprint
inputstr = ['ШАЛАШ', 'КАЗАК', 'ДЕД', 'ДОХОД', '13231', 'hgfhjgfjhgfjhjhgfj', 'dfjh']

with open('C:\\tr1\\polid.csv', 'r+', encoding='utf-8') as file1:
    reader = csv.reader(file1,delimiter='|')
    writer = csv.writer(file1,delimiter='|')
    # writer.writerow(['indent', 'string','asa'])
    # writer.writerow(['asdadas','asda','asdas'])
    print(file1.readlines())

