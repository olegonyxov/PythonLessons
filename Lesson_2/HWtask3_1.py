t = int(input("input time:"))
v = int(input("input Vasya's sspeed:"))
z = v * t
if v > 0 and 100 > z > 0:
    print(z, "'th km")
else:
    print("уехал домой")
while 100 > z > 0:
    t = int(input("input time:"))
    v = int(input("input Vasya's sspeed:"))
    z = (v * t) + z

    if 100 > z > 0:
        print(z, "'th km")
    else:
        print("Васи больше нет :((")
        break
