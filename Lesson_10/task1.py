import csv

wordlist = ['asdfasdf', 'sdfasdf', 'fghfdgh', 'sdfgdsg', 'dfgsdg', 'asdfdsa', 'fdsasdf']
# inputstr = input('input your words:')
# inputindent = input('input indent number:')
inputindent = int("3")
fieldnames = ('indent', 'string', 'polindrome')


def makelist():
    while True:
        inputstr = input('input your words:')
        wordlist.append(inputstr)
        if inputstr == "":
            del wordlist[-1]
            break
    return wordlist


def write_words():
    with open('C:\\tr1\\polid.csv', 'r+', encoding='utf-8') as file1:
        writer = csv.DictWriter(file1, fieldnames=fieldnames,delimiter=' ')
        for word in wordlist:
            if word == word[::-1]:
                writer.writerow({'indent': make_indent(), "string": word, 'polindrome': 'Yes'})
            else:
                writer.writerow({'indent': make_indent(), "string": word, 'polindrome': 'NO'})


def make_indent():
    indent = ""
    with open('C:\\tr1\\polid.csv', 'r+', encoding='utf-8') as file1:
        reader = csv.DictReader(file1, fieldnames=fieldnames,delimiter=' ')
        for row in reader:
            print(row)
            if inputindent < 0 and abs(inputindent) >= len(row["indent"]):
                del row['indent']
                indent = ""
            else:
                indent = str((inputindent + len(row['indent'])) * " ")
    return indent


write_words()
