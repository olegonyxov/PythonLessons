xs = int(input("input x start"))
ys = int(input("input y start"))
x2 = int(input("input x coord 2"))
y2 = int(input('input y coord 2'))
success1 = 0
success2 = 0
if 0 < xs and ys and x2 and y2 < 8:

    hod1 = (-2, 2)
    hod2 = (-1, 1)
    for x in hod1:
        xend1 = xs + x
        for y in hod2:
            yend1 = ys + y
            if xend1 == x2 and yend1 == y2:
                print('Конь Хадить Г')
                success1 = 1

    for x in hod2:
        xend2 = xs + x
        for y in hod1:
            yend2 = ys + y
            if xend2 == x2 and yend2 == y2:
                print('Конь Хадить Г')
                success2 = 1
else:
    print('кончилась доска')
if success1 == 1 or success2 == 1:
    print("ok")
else:
    print("не ок")
