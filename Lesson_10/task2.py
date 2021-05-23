import re


def checkline():
    with open('C:\\tr1\\polid.txt', 'r', encoding='utf-8') as file1:
        for line in file1.readlines():
            line = re.match(r"\w+", line)[0]
            if line == line[::-1]:
                print("слово", line, "является палиндромом")

checkline()
