import datetime

import requests

vline = str()
f2 = open('C:/tr1/t7_3.txt', 'w+')
f2.writelines('Дата    Температура днем  По ощущениям')
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=Odesa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"
response = requests.get(url).json()
for i in response['list']:
    day_z = str(datetime.datetime.fromtimestamp(i['dt']))
    zline = day_z[0:10], "   ", (i['temp']['day']), "   ", (i['feels_like']['day'])
    zline = str(zline).replace(",", "").replace('\'', "").replace(')', "").replace('(', "")
    f2.writelines("\n")
    f2.writelines(zline)
f2 = open('C:/tr1/t7_3.txt', 'r')
print(f2.read())
f2.close()
