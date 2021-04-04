xlist = (3, 6, 9, 3, 0)
sumx = sum((int(x1) for x1 in xlist))
print('сумма равна', sumx)
xlist = xlist[0:-1]
print(xlist)
m = 0
s = 1
while m < int(len(xlist)):
    s = s * xlist[m]
    m = m + 1
print('произведение равно:', s)
print(xlist)
print('среднее арифметическое равно', sumx / len(xlist))
m = 0
for i in xlist:
    if i > xlist[m]:
        i = xlist[m]
        m = m + 1
        print(xlist[m], m)
