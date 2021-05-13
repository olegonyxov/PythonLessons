import random

string = 'somebody_email@gmail.com'


def change_char():
    slices = string.split('@')
    endlist = []
    for word in slices:
        b = int(len(word) / 3)
        for a in range(b):
            i = random.randint(0, (len(word) - 1))
            word = word.replace(word[i], '*')
        endlist.append(word)
    endadress = "@".join(endlist)
    return endadress


print(change_char())
