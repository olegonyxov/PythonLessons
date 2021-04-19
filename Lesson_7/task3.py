import requests
import datetime
import json

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=Odesa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"
response = requests.get(url).json()
# print(response)
# print(response.keys())
for i in response['list']:
    print(i['dt'], (i['temp']['day']), (i['feels_like']['day']))
    # day_z = (datetime.timedelta(seconds=i['dt']))
    # print(day_z.strtime())


