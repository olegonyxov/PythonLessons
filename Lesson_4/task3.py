a = int(input('input a:'))
b = int(input('input b:'))
alist = list(range(a, (b + 1)))
blist = list(range(a, (b - 1), -1))
if a < b:
    print(alist)
else:
    print(blist)
#почемуто способы с перевертышами и присвоением выдают у меня пустую строку, хотя гугл говорит, что должно работать...