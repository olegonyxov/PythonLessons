import csv
import re


def checkshtring():
    if str1 == re.match(r'^\w{2}\d{4}\w{2}', str1)[0]:
        return "OK"


def translate():
    with open(translatefile, "r", encoding='utf-8') as file2:
        reader = csv.DictReader(file2)
        for row in reader:
            if str1[0:2] in row["eng"]:
                str1.replace((str1[0:2]), row["ukr"])


def checkregion():
    print(checkshtring())
    if checkshtring() == "OK":
        with open(filename, "r", encoding='utf-8') as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                if str1[0:2] in (row["Код 2004"], ["Код 2013"]):
                    print("Номер зарегестрирован в ", row["Регіон"])
    else:
        print("Строка не является автомобильным номером")


if __name__ == "__main__":
    # str1 = "АН3231АЕ"
    str1 = input(str("Input car Number:"))
    filename = 'C:\\tr1\\ua_auto.csv'
    translatefile = 'C:\\tr1\\translateautonumb.csv'
    translate()
    checkregion()
