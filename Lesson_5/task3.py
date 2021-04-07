side1 = int(input('введите длинну первой стороны:'))
side2 = int(input('введите второй стороны :'))
ty2 = int(input('введите тип фигуры:1 = треугольник, 2= квадрат:'))
def square_all(side1,side2,ty2):
    if ty2 == 1:
        return int(side1*side2/2)
    else:
        return int(side1*side1)

print('Площадь=',square_all(side1,side2,ty2))
