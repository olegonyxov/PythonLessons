def checkline():
    inputstring = input("input some string:")
    if inputstring == inputstring[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(checkline())
