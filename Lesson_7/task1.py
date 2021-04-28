isring = str(input('Input some string :'))
def byw(fnc):
    pl = fnc().split(' ')
    print(pl)
    return fnc


@byw
def first():
    return isring


first()
