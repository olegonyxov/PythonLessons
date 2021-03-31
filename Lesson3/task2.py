xl1 = input("ведите число :")
xl = float(xl1)
xl = abs(xl)%1
print(xl)
# почему не правильно работает ?
# y = xl**2//xl
# xl = xl -y
# тоже нет
xl = str(xl)
xl = list(xl)
print(xl[2])


