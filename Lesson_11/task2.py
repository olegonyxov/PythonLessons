import random

string = 'somebody_email@gmail.com'


def change_char():
    slices = string.split('@')
    endlist = []
    for word in slices:
        a = 0
        while a < (len(word) / 4):
            i = random.randint(0, (len(word) - 1))
            word = word.replace(word[i], '*')
            a += 1
        endlist.append(word)
    endadress = "@".join(endlist)
    return endadress


print(change_char())
