import csv
import re


def checkshtring():
    # input_string = str1
    input_string = input("Введите номер авто:")
    if input_string == re.match(r'^\w{2}\d{4}\w{2}', input_string)[0]:
        return input_string, print("Строка является автомобильным номером")
    else:
        print("Строка не является автомобильным номером")


def translate():
    with open(translatefile, "r", encoding='utf-8') as file2:
        reader = csv.DictReader(file2)
        workstring = checkshtring()[0]
        for row in reader:
            symb2 = re.match(r'^\w{2}', workstring)[0]
            if symb2 in row["eng"]:
                workstring.replace(symb2, row["ukr"])
    return workstring


def checkregion():
    workstring = translate()
    with open(filename, "r", encoding='utf-8') as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            if re.match(r'^\w{2}', workstring)[0] in (row["Код 2004"], row["Код 2013"]):
                return "Номер зарегестрирован в "+row["Регіон"]
        else:
            return "Строка не найдена в таблице регионов"


if __name__ == "__main__":

    filename = 'C:\\tr1\\ua_auto.csv'
    translatefile = 'C:\\tr1\\translateautonumb.csv'
    print(checkregion())
    # str1 = "АН3231АЕ"
