x1 = int(input('input number:'))


def is_prime(x2, res):
    for xs in list(range(2, x1, 1)):
        if x2 % xs == 0:
            res = 1
    if res == 1:
        return False
    else:
        return True


print(is_prime(x1, 0))
