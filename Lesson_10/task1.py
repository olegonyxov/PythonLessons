import csv

inputstr = str(input('input some strong:'))
inputnum = int(input("input space arg:"))
x = 1
while inputstr != 0:
    with open('C:\\tr1\\polid.csv', 'w', encoding='utf-8') as file1:
        reader = csv.DictReader(file1, fieldnames=['indent', 'string', 'palindrome'])
        writer = csv.DictWriter(file1, fieldnames=['indent', 'string', 'palindrome'])
        if inputnum > 0:
            inputnum = " " * inputnum
        else:  # TODO
            inputnum = ""
        if inputstr == inputstr[::-1]:
            writer.writerow({'indent': inputnum, 'string': inputstr, 'palindrome': 'YES'})
        else:
            writer.writerow({'indent': inputnum, 'string': inputstr, 'palindrome': 'NO'})
