def movelist():
    if inputint < 0:
        finlist = inputlist[abs(inputint):] + inputlist[0:abs(inputint)]
    else:
        finlist = inputlist[(len(inputlist) - inputint):] + inputlist[0:(len(inputlist) - inputint):]
    return finlist


if __name__ == "__main__":
    inputlist = input('input list:')
    inputint = int(input('input move parameter:'))
    print(movelist())
