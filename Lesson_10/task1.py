
import csv
inputstr = ['ШАЛАШ', 'КАЗАК', 'ДЕД', 'ДОХОД', '13231','hgfhjgfjhgfjhjhgfj','dfjh']
with open('polid.csv', 'w+',encoding='utf-8') as file1:
    reader=csv.reader(file1)

    writer=csv.writer(file1)
    while True:
        inputstring = str(input("Input some string:"))
        writer.writerow(inputstr)
        if inputstring == "":
            break



# inputstr = ['ШАЛАШ', 'КАЗАК', 'ДЕД', 'ДОХОД', '13231','hgfhjgfjhgfjhjhgfj','dfjh']
# inputint = 3
#
# for i in inputstr:
#     if i == i[::-1]:
#         print(i)




