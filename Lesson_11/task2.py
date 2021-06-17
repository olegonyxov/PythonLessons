import random


def change_char(string):
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


if __name__ == "__main__":
    print(change_char('somebody_email@gmail.com'))