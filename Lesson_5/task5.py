ab = input("input AB:")

def out_sq():
    sab = int(ab) * int(ab)
    pab = int(ab) * 4
    dab = int(ab)* 2**0.5
    return sab, pab, dab

print(out_sq())
