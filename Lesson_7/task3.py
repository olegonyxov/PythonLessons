import datetime

import requests

iday = str(input("Введите количество дней:"))
icity = str(input('Введите название города:'))
url = "http://api.openweathermap.org/data/2.5/forecast/daily"
pars = {'cnt': iday, 'q': icity, 'units': 'metric', 'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
response = requests.get(url, params=pars)
response = response.json()

def makefile(ff):
    global f2
    filename = str('C:\\tr1\\' + str(datetime.date.today()) +"-"+icity+"-" + iday + '-days-weather-forecast.txt')
    with open(filename, "w") as f2:  # создаем или перезаписываем
        f2.writelines('Дата   Температура днем По ощ.  Ночью')
        ff()
        return f2


@makefile
def makelines():
    for i in response['list']:
        day_z = str(datetime.date.fromtimestamp(i['dt']))
        datalines = str(day_z + '\t' + str(i['temp']['day'])
                        + '\t' + str(i['feels_like']['day']) + '\t' + str(i['temp']['night']))
        f2.writelines("\n")
        f2.writelines(datalines)


print(makelines)  # ооздаем и проверяем имя и путь (печатать в условии нет)
