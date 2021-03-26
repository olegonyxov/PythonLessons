t = int(input("input time:"))
v = int(input("input Vasya's sspeed:"))
z = v * t
if v > 0 and 100 > z > 0:
    print(z, "km")
else:
    print("0")
    print("уехал домой")
