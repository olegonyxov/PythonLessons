t = int(input("input time:"))
v = int(input("input Vasya's speed:"))
z = v * t
if v >= 0 and 100 >= z >= 0:
    print(z, "km")
else:
    print("уехал домой")
