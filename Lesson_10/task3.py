


i_indent = 3

def checklinew():
    newlist = []
    with open('C:\\tr1\\polid.txt', 'r', encoding='utf-8') as file1:
        for line in file1.readlines():
            if i_indent > 0:
                newlist.append(line.rjust((len(line)+i_indent), " "))
            elif i_indent < 0:
                a=1
    return newlist


def writenew():
    with open('C:\\tr1\\polid.txt', 'w', encoding='utf-8') as file1:
        for line in checklinew():
            file1.write(line)


print(checklinew())

writenew()



