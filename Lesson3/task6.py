xs = int(input("input x start:"))
ys = int(input("input y start:"))
x2 = int(input("input x coord 2:"))
y2 = int(input("input y coord 2:"))
success = 0
if 0 < xs < 8 and 0 < ys < 8 and 0 < x2 < 8 and 0 < y2 < 8:
    dlist = (-2, -1, 1, 2)
    for x in dlist:
        for y in dlist: 
            if abs(x) != abs(y) and x == x2 - xs and y == y2 - ys:
                success = 1
else:
    print('out of desk')
if success == 1:
    print('Correct move!')
else:
    print('Incorrect move!')
