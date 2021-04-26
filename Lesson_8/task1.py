import argparse
import time
from datetime import timedelta, datetime

import requests

parser = argparse.ArgumentParser(description="currency_checker")
parser.add_argument('inputincur')
parser.add_argument('outcur')
parser.add_argument('amcur')
parser.add_argument('start_date')
args = parser.parse_args()
argsdict = vars(args)
incur = argsdict['inputincur']
outcur = argsdict['outcur']
amcur = argsdict['amcur']
input_date = argsdict['start_date']
start_date = datetime.strptime(input_date, '%Y-%m-%d')
today_date = datetime.now()
daylist = list()
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


def getresponse():
    print('date:    from: to:    rate :    result:')
    for date in daylist:
        pars = {'from': incur, 'to': outcur, 'amount': amcur, 'date': date}
        response = requests.get(url, params=pars)
        data = response.json()
        print(data['date'], incur, outcur, amcur, data['info']['rate'], data['result'])
        time.sleep(1)


if __name__ == "__main__":
    checkdate(), make_daylist(), getresponse()
