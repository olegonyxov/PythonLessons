import random

n = 1
while n <= 3:
    xd = int(input("input number 1 to 10 (3 tries):"))
    rd = random.randint(1, 10)
    n += 1
    if xd == rd:
        print("You Won!!!")
    else:
        print("You Loose!")
