xl1 = input("ведите число :")
xl = float(xl1)
xl = abs(xl) % 1
print('дробная часть числа:', xl)
xl = str(xl)
xl = list(xl)
print('первая цифра после десятичной точки:', xl[2])
# почему не правильно работает ?
# y = xl**2//xl
# xl = xl -y
# тоже нет
# y1 = float(xl1)
# z1 = abs(y1) - abs(int(y1))
# print(z1)
# z1 = str(z1)
# z1 = list(z1)
# print(z1[2])
