x1 = int(input("введите число:"))
xlist = list(range(x1 + 1))
n = 1
y = 1
while n <= x1:
    y = y * n
    n = n + 1
print('факториал числа', x1, '=', y)

