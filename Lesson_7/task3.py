import requests
import datetime
import json

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=Odesa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"
response = requests.get(url).json()
# print(response)
# print(response.keys())
# print(response['list'])
for i in response['list']:
    print(i['dt'], (i['temp']['day']), (i['feels_like']['day']))
    print(str(datetime.timedelta(hours=i['dt'])))

