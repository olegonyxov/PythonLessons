import csv


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

        for word in wordlist:
            if word == word[::-1]:
                writer.writerow({"string": word, 'palindrome': 'Yes'})
            else:
                writer.writerow({"string": word, 'palindrome': 'NO'})



def make_indent():
    indent = ""
    with open('C:\\tr1\\polid.csv', 'r', encoding='utf-8') as file2:
        reader = csv.DictReader(file2, fieldnames=fieldnames, delimiter=' ')
        reader.line_num = 1
        for row in reader:
            print('fgjhgfhg')
            print(row)
            if inputindent < 0 and abs(inputindent) >= len(row["indent"]) or inputindent == 0:
                pass
            else:
                indent = (len(row['indent']) + int(inputindent)) * " "

    return indent


if __name__ == "__main__":
    inputindent = int(input('input indent number:'))
    fieldnames = ('indent', 'string', 'palindrome')
    make_indent()
    wordlist = []
    makelist()
    write_words()
