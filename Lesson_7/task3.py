import requests
import datetime
import json
with open('C:/tr1/t7_3.dat', 'w+') as f2:
    f2.writelines('Дата Температура днем  По ощущениям')
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=Odesa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"
    response = requests.get(url).json()
    for i in response['list']:
        day_z = str(datetime.datetime.fromtimestamp(i['dt']))
        z = day_z[0:10], (i['temp']['day']), (i['feels_like']['day'])
        print(z)
        f2.writelines("\n")
        f2.writelines(str(z))
with open('C:/tr1/t7_3.dat', 'r') as f3:
    print(f3.read())

