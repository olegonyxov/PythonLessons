import datetime

dd = int(input("Введите день:"))
mm = int(input("Введите месяц:"))
yy = int(input("Введите год:"))

def is_date():
    try:
        datetime.date(yy, mm, dd)
        return True

    except:
        return False
print(is_date())
