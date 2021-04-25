import time
from datetime import timedelta, datetime

import requests

incur = 'USD'
outcur = 'UAH'
amcur = '99'
# start_date =input()
input_date = '2021-04-23'
start_date = datetime.strptime(input_date, '%Y-%m-%d')
today_date = datetime.now()
daylist = list()
finall = list()
url = 'https://api.exchangerate.host/convert'


def checkdate():
    global start_date
    if start_date < today_date:
        pass
    else:
        start_date = today_date
        return start_date


def make_daylist():
    fake_date = start_date
    while fake_date <= today_date:
        daylist.append(fake_date.date())
        fake_date += timedelta(1)
    return daylist


def getresponse():
    for date in daylist:
        pars = {'from': incur, 'to': outcur, 'amount': amcur, 'date': date}
        response = requests.get(url, params=pars)
        data = response.json()
        print(data['date'], incur, outcur, amcur, data['info']['rate'], data['result'])
        time.sleep(1)


checkdate()
make_daylist()
getresponse()
