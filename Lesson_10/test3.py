import re


def work_indent():
    input_indent = int(input("input indent parameter:"))
    wordlist = []
    with open('C:\\tr1\\polid.txt', 'r', encoding='utf-8') as file1:
        for line in file1.readlines():
            clearline = re.search(r"\w+", line)[0] + "\n"
            ex_indent = len(line) - len(clearline)
            if input_indent < 0:
                if input_indent < ex_indent:
                    line = " " * (ex_indent + input_indent) + clearline
                else:
                    line = clearline
            else:
                line = " " * input_indent + line
            wordlist.append(line)
    return wordlist


def write_file():
    with open('C:\\tr1\\polid.txt', 'w', encoding='utf-8') as file1:
        file1.writelines(work_indent())
    return file1


if __name__ == "__main__":
    write_file()
    # print(work_indent())
