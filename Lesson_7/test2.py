import datetime as dt

import requests

iday = '3'
icity = 'Odesa'
# iday = str(input("Введите количество дней:"))
# icity = str(input('Введите название города:'))
url = "http://api.openweathermap.org/data/2.5/forecast/daily"
pars = {'cnt': iday, 'q': icity, 'units': 'metric', 'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
response = requests.get(url, params=pars)
response = response.json()
# print(response)  # проверяем ответ
datelist = list()
print(response['list'])
with open('C:\\tr1\\myfile.txt', 'w') as file:
    for day in response['list']:
        daydate = dt.date.fromtimestamp(day['dt'])
        daydate = dt.date.strftime(daydate, '%Y-%m-%d')
        daytd = str(day['temp']['day'])
        dayfl = str(day['feels_like']['day'])
        daytn = str(day['temp']['night'])
        daywath = daydate + '\t' + daytd + '\t' + dayfl + '\t' + daytn
        file.writelines(daywath)


print(daywath)
