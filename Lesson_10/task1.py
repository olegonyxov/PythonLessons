import csv


def makelist():
    while True:
        inputstr = input('input your words:')
        wordlist.append(inputstr)
        if inputstr == "":
            del wordlist[-1]
            break
    move_list()
    return wordlist


def write_file():
    with open('C:\\tr1\\polid.csv', 'w+', encoding='utf-8') as file1:
        writer = csv.DictWriter(file1, fieldnames=fieldnames, delimiter='|')
        for word in wordlist:
            if word == word[::-1]:
                writer.writerow({"string": word, 'palindrome': 'Yes'})
            else:
                writer.writerow({"string": word, 'palindrome': 'NO'})


def move_list():
    inputmoveint = input('input indent number:')
    if inputmoveint == "":
        pass
    elif inputmoveint != 0:
        intm = int(inputmoveint)
        templist = wordlist[0:intm]
        wordlist.extend(templist)
        del wordlist[0:len(templist)]
    return wordlist


if __name__ == "__main__":
    fieldnames = ('string', 'palindrome')
    wordlist = []
    makelist()
    write_file()
