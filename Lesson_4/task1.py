x = input('input start length:')
y = input('input length to find a day:')
x = float(x)
y = float(y)
n = 1
while x < y:
    x = x + x / 10
    n = n + 1
print(n)

