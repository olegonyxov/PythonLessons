import re


def check_numb(pnumber):
    renew = "".join(re.findall(r'\d*', pnumber))
    if re.search(r'^\d{3}', renew)[0] == "380":
        renew = renew[2:-1]
    if len(renew) == 10:
        print("{} {} {}-{}-{}".format("(+38)", renew[0:3], renew[3:6], renew[6:8], renew[8:10]))
    else:
        print("incorrect input")


def check_input(pnumber):
    if re.findall(r'\d', pnumber) == re.findall(r'\w', pnumber):
        check_numb(pnumber)
    else:
        print("incorrect input")


if __name__ == "__main__":
    i_string = input(str("Input phone number :"))
    check_input(i_string)
