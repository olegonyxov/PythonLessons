import re


def check_az():
    if re.search(r"\w[a-z]", istring):
        return True
    else:
        print("Хотя бы одна маленькая буква")


def check_az2():
    if re.search(r"\w[A-Z]", istring):
        return True
    else:
        print("Хотя бы одна Большая буква")


def check_09():
    if re.search(r"\d", istring):
        return True
    else:
        print("Хотя бы одна цифра")


def check_symb():
    if re.search(r"\W", istring):
        return True
    else:
        print("Хотя бы однид символ $#@-+= ")


def check_len():
    if len(istring) > 8:
        return True

    else:
        print("Хотя бы 8 символов")


if __name__ == "__main__":
    while True:  # пачку скурил
        istring = input("input your password:")
        if all([check_az(), check_az2(), check_09(), check_symb(), check_len()]):
            print("password accepted")
            break

# istring = input("Input new password:")
# istring = "dasdasdASDASD12312#@+=-$"
