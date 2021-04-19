isring = str(input('Input some string :'))
# isring = 'asdas asd as dasd asd'
def byw(fnc):
    pl = fnc().split(' ')
    print(pl)
    return fnc


@byw
def first():
    return isring


first()
