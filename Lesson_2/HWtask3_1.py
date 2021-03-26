t = int(input("input time:"))
v = int(input("input Vasya's speed:"))
z = v * t
if v > 0 and 100 > z > 0:
    print("Vasia is at", z, "'th km")
else:
    print("уехал домой")
while 100 > z > 0:
    t = int(input("input time to search for Vasia:"))
    v = int(input("input Vasya's last speed:"))
    z = (v * t) + z

    if 100 > z > 0:
        print("Vasia is at", z, "'th km")
    else:
        print("Васи больше нет :((")
        break
