i = 1
n = 1
xlist = list()
while xi != 0:
    xi = int(input('input x :'))
    xlist.append(xi)
    n = n + 1
print('количество введенных чисел', n - 1)
sumx = sum((int(x1) for x1 in xlist))
print('сумма равна',sumx)
xlist = xlist[0:-1]
m = 0
s = 1
while m < int(len(xlist)):
    s = s * xlist[m]
    m = m + 1
print('произведение равно:', s)
print('среднее арифметическое равно', sumx / int(len(xlist)))
m = 0
for i in xlist:
    if i > xlist[m]:
        i = xlist[m]
        m = m + 1
print('наибольшее число :',xlist[m],'под индексом ', m)
