import re


def checkline():
    wordlist = []
    with open('C:\\tr1\\polid.txt', 'r', encoding='utf-8') as file1:
        for line in file1.readlines():
            line = re.search(r"\w+", line)[0]  # для всех indent кейсоу
            if line == line[::-1]:
                wordlist.append(line)
    return wordlist


print(checkline())
