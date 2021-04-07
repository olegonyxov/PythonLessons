side1 = input('введите длинну первой стороны:')
side2 = input('введите второй стороны :')
ty1 = input('если тип - квадрат: введите 1')


def square_all(ty1):
    if ty1 == '1':
        return int(side1) * int(side1)
    else:
        return int(side1) * int(side2) / 2


print('Площадь=', square_all(ty1))
