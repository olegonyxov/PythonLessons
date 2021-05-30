import re


def check_len(pnumber):
    renew = "".join(re.findall(r'\d*', pnumber))
    if re.search(r'^\d{3}', renew)[0] == "380":
        renew = renew.replace("38", "", 1)
    if len(renew) == 10:
        return "{} {} {}-{}-{}".format("(+38)", renew[0:3], renew[3:6], renew[6:8], renew[8:10])
    else:
        print("incorrect inputa")
        return False


def check_input(pnumber):
    if re.findall(r'\d', pnumber) == re.findall(r'\w', pnumber):
        print(check_len(pnumber))
        return True
    else:
        print("incorrect inputb")
        return False


if __name__ == "__main__":
    i_string = input("Input phone number :")
    check_input(i_string)
