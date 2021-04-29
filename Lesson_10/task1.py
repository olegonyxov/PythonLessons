import csv

inputstr = ['ШАЛАШ', 'КАЗАК', 'ДЕД', 'ДОХОД', '13231', 'hgfhjgfjhgfjhjhgfj', 'dfjh']

with open('C:\\tr1\\polid.csv', 'w+', encoding='utf-8') as file1:
    reader = csv.reader(file1)
    writer = csv.writer(file1)
    writer.writerow(['indent', 'string','asa'])
    for row[2] in reader.line_num

    # while True:
    #     inputstring = str(input("Input some string:"))
    #     if inputstring == "":
    #         break
    #     for i in reader['string']:
    #         writer.writerow(inputstr)

# inputstr = ['ШАЛАШ', 'КАЗАК', 'ДЕД', 'ДОХОД', '13231','hgfhjgfjhgfjhjhgfj','dfjh']
# inputint = 3
#
# for i in inputstr:
#     if i == i[::-1]:
#         print(i)
