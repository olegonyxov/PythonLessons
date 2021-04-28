import datetime as dt
import requests

idays = str(input("Введите количество дней:"))
icity = str(input('Введите название города:'))
url = "http://api.openweathermap.org/data/2.5/forecast/daily"
pars = {'cnt': idays, 'q': icity, 'units': 'metric', 'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
response = requests.get(url, params=pars)
response = response.json()
datelist = list()


def make_datelist():
    for day in response['list']:
        daydate = dt.date.fromtimestamp(day['dt'])
        daydate = dt.date.strftime(daydate, '%Y-%m-%d')
        datelist.append(daydate)


def make_name():
    filename = 'C:\\tr1\\'
    templist = datelist[1], icity, idays, 'days', 'weather', 'forecast'
    filename = filename + "-".join(templist) + ".txt"
    return filename


def make_file():
    with open(make_name(), 'w') as file:
        file.writelines('Дата   Температура днем По ощ.  Ночью')
        file.writelines('\n')
        i = 0
        for day in response['list']:
            daytd = str(day['temp']['day'])
            dayfl = str(day['feels_like']['day'])
            daytn = str(day['temp']['night'])
            daywath = datelist[i] + '\t' + daytd + '\t' + dayfl + '\t' + daytn
            i = i + 1
            file.writelines(daywath)
            file.writelines("\n")

if __name__ == '__main__':
    make_datelist()
    make_name()
    make_file()
