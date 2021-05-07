import csv

# wordlist = ['asdfasdf', 'sdfasdf', 'fghfdgh', 'sdfgdsg', 'dfgsdg', 'asdfdsa', 'fdsasdf']
# inputindent = int("3")
fieldnames = ('indent', 'string', 'palindrome')
wordlist = []
inputindent = int(input('input indent number:'))


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
        writer = csv.DictWriter(file1, fieldnames=fieldnames, delimiter=' ')
        make_indent()
        for word in wordlist:
            if word == word[::-1]:
                writer.writerow({'indent': make_indent(), "string": word, 'palindrome': 'Yes'})
            else:
                writer.writerow({'indent': make_indent(), "string": word, 'palindrome': 'NO'})


def make_indent():
    indent = ""
    with open('C:\\tr1\\polid.csv', 'r+', encoding='utf-8') as file1:
        reader = csv.DictReader(file1, fieldnames=fieldnames, delimiter=' ')
        for row in reader:
            if inputindent < 0 and abs(inputindent) >= len(row["indent"]):
                pass
            else:
                indent = (len(row['indent'])+int(inputindent)) * " "
    return indent


makelist()
write_words()

