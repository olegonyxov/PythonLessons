import re

i_indent = -1


def checklinew():
    newlist = []
    with open('C:\\tr1\\polid.txt', 'r', encoding='utf-8') as file1:
        for line in file1.readlines():
            tlength = len(re.search(r"\w+",line)[0])+i_indent
            if tlength > 0:
                line =
            print(tlength)
            print(line)
    return newlist


checklinew()
