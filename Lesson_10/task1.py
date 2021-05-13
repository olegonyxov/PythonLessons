import csv


def makelist():
    while True:
        inputedstring = input('input your words:')
        wordlist.append(inputedstring)
        if inputedstring == "":
            del wordlist[-1]
            break
    move_list()
    return wordlist


def write_file():
    with open('C:\\tr1\\polid.csv', 'w+', encoding='utf-8') as file1:
        writer = csv.DictWriter(file1, fieldnames=fieldnames, delimiter=':')
        for word in makelist():
            if word == word[::-1]:
                writer.writerow({"string": word, 'palindrome': 'palindrome'})
            else:
                writer.writerow({"string": word, 'palindrome': 'simple word'})


#  KISS
def move_list():
    inputedmovevar = input('input move number:')
    if inputedmovevar == "":
        pass
    elif inputedmovevar != 0:
        templist = wordlist[0:int(inputedmovevar)]
        wordlist.extend(templist)
        del wordlist[0:len(templist)]
    return wordlist


if __name__ == "__main__":
    fieldnames = ('string', 'palindrome')
    wordlist = []
    write_file()
