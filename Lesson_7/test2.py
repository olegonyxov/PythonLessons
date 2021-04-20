import datetime

import requests
iday = '3'
icity = 'London'
# iday = str(input("Введите количество дней:"))
# icity = str(input('Введите название города:'))
pars = {'q': icity, 'cnt': iday}  # https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests
f2 = open('C:/tr1/t7_3.txt', 'w+')
# раз сказали что можно криво
f2.writelines('Дата   Температура днем  По ощ.   Ночью')
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=London&cnt=1&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"
response = requests.get(url, params=pars)  # с params работает через раз походу задракоили сайт
print(response.headers)
response = response.json()
print(response)
for i in response['list']:
    day_z = str(datetime.datetime.fromtimestamp(i['dt']))
    zline = day_z[0:10], "   ", (i['temp']['day']), "   ", (i['feels_like']['day'], "   ", (i['temp']['night']))
    zline = str(zline).replace(",", "").replace("'", "").replace(')', "").replace('(', "")
    f2.writelines("\n")
    f2.writelines(zline)
f2 = open('C:/tr1/t7_3.txt', 'r')
print(f2.read())
f2.close()
