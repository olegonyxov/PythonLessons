import re
import csv

def checkshtring():
    if str1 == re.search(r'^\w{2}\d{4}\w{2}', str1)[0]:
        return "OK"

def checkregion():
    print(checkshtring())
    if checkshtring() == "OK":
        with open(filename, "r", encoding='utf-8') as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                print(row["Код 2004"])
                if str1[0:2] == row["Код 2004"] or str1[0:2] ==row["Код 2013"]:
                    print("Номер зарегестрирован в ", row["Регіон"])
    else:
        print("Строка не является автомобильным номером")


if __name__ == "__main__":
    str1 = "AI3231AE"
    filename = 'C:\\tr1\\ua_auto.csv'
    checkregion()