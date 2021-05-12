import csv


def makelist():
    while True:
        inputstr = input('input your words:')
        wordlist.append(inputstr)
        if inputstr == "":
            del wordlist[-1]
            print(wordlist)
            print(type(wordlist))
            break
    try:
        move_list()
    except ValueError:
        pass
    return wordlist


def write_words():
    with open('C:\\tr1\\polid.csv', 'w+', encoding='utf-8') as file1:
        writer = csv.DictWriter(file1, fieldnames=fieldnames, delimiter='|')
        for word in wordlist:
            if word == word[::-1]:
                writer.writerow({"string": word, 'palindrome': 'Yes'})
            else:
                writer.writerow({"string": word, 'palindrome': 'NO'})


def move_list():
    inputmoveint = input('input indent number:')
    intm = int(inputmoveint)
    templist = wordlist[0:intm]
    wordlist.extend(templist)
    del wordlist[0:len(templist)]
    print(wordlist)
    return wordlist


if __name__ == "__main__":
    fieldnames = ('string', 'palindrome')
    wordlist = []
    makelist()
    write_words()
