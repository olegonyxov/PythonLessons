xi = 1
n = 1
xlist = list()
while xi != 0:
    xi = int(input('input x :'))
    xlist.append(xi)
    n = n + 1
print('количество введенных чисел', n - 2)
sumx = sum((int(x1) for x1 in xlist))
print('сумма равна', sumx)
xlist = xlist[0:-1]
m = 0
s = 1
while m < int(len(xlist)):
    s = s * xlist[m]
    m = m + 1
print('произведение равно:', s)
print('среднее арифметическое равно', sumx / int(len(xlist)))
print('наибольшее число :', max(xlist), 'под индексом ', xlist.index(max(xlist)))

evenlist = list()
oddlist = list()
for i in xlist:
    if i % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print('количество четных чисел =', len(evenlist))
print('количество нечетных чисел =', len(oddlist))
x1list = list(set(xlist))
x1list.remove(max(x1list))
print('второе по величине чмсло', max(x1list))
rlist = list()
for i in xlist:
    if i == max(xlist):
        rlist.append(i)
print('количество элементов равных максимальному:', len(rlist))
