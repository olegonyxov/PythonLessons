def if_c(inputtempin):
    return "Кельвин:" + str(inputtempin + 273.5) + "Цельсий:" + str(inputtempin) + "Фарингейт:" + str(
        inputtempin * 1.8 + 32)


def if_k(inputtempin):
    return "Кельвин:" + str(inputtempin) + "Цельсий:" + str(inputtempin - 273.5) + "Фарингейт:" + str(
        inputtempin * 1.8 - 459.67)


def if_f(inputtempin):
    return "Кельвин:" + str(int(inputtempin + 459.67 / 1.8)) + "Цельсий:" + str(
        int((inputtempin - 32) / 1.8)) + "Фарингейт:" + str(inputtempin)


def temperatures(temp, inputscalein):
    tempout = []
    if inputscalein == "c":
        tempout = if_c(temp)
    if inputscalein == "k":
        tempout = if_k(temp)
    if inputscalein == "f":
        tempout = if_f(temp)
    return tempout


if __name__ == "__main__":
    inputtemp = int(input('input temperature:'))
    inputscale = str(input('input scale:'))
    print(temperatures(inputtemp, inputscale))
