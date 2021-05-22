import re


def check_numb(str1):
    renew = "".join(re.findall(r'\d*\d+|\d+', str1))
    if renew[0] == "3":
        renew = renew[2:-1]
    if len(renew) == 10:
        print("{} {} {}-{}-{}".format("(+38)", renew[0:3], renew[3:6], renew[6:8], renew[8:10]))
    else:
        print("incorrect input")


def check_input(str1):
    if re.findall(r'\d', str1) == re.findall(r'\w', str1):
        check_numb(str1)
    else:
        print("incorrect input")


if __name__ == "__main__":
    str1 = input(str("Input phone number :"))
    check_input(str1)
