import csv

#
# inputstr = str(input('input some strong:'))
# inputnum = int(input("input space arg:"))

inputstr = "lal"
while inputstr != "":
    inputstr = str(input('input some strong:'))
    with open('C:\\tr1\\polid.csv', 'r+', encoding='utf-8') as file1:
        reader = csv.DictReader(file1, fieldnames=['indent', 'string', 'palindrome'])
        writer = csv.DictWriter(file1, fieldnames=['indent', 'string', 'palindrome'])

        if inputstr == inputstr[::-1]:
            writer.writerow({'string': inputstr})
            writer.writerow({'palindrome': 'YES'})
        else:
            writer.writerow({'string': inputstr})
            writer.writerow({'palindrome': 'YES'})
# inputnum = int(input("input space arg:"))
# inputnum = '3'
# if int(inputnum) > 0:
#     inputnum = str(" " * int(inputnum))
#     writer.writerow({'indent': inputnum})






