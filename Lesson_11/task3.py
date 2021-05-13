string = "What makes a good man"


def longest():
    lengthlist = []
    wordlist = string.split(' ')
    for word in wordlist:
        lengthlist.append(int(len(word)))
    return wordlist[lengthlist.index(max(lengthlist))]


print(longest())
