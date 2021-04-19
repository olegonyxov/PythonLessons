isring = str(input('Input some string :'))


def byw(ff):
    global isring
    isring = isring.split(' ')
    return ff


@byw
def printw():
    print(isring)


printw()
