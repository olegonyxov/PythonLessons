def checklinew(i_indent):
    newlist = []
    with open('C:\\tr1\\polid.txt', 'r', encoding='utf-8') as file1:
        for line in file1.readlines():
            if i_indent >= 0:
                newlist.append(line.rjust((len(line) + i_indent), " "))
            if i_indent < 0:
                indent_count = line.rfind(" ") + 1
                if abs(i_indent) < indent_count:
                    line = line.replace(" ", "", (abs(i_indent)))
                else:  # abs(i_indent) >= indent_count:
                    line = line[indent_count:]
                newlist.append(line)
    print(newlist)
    return newlist


def writenew(i_indent):
    with open('C:\\tr1\\polid.txt', 'r+', encoding='utf-8') as file1:
        for line in checklinew(i_indent):
            file1.write(line)


if __name__ == "__main__":
    input_indent = input(str("input needed indent:"))
    writenew(input_indent)
