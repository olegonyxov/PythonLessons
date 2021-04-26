import argparse
from datetime import timedelta, datetime

import requests

parser = argparse.ArgumentParser(description="currency_checker")
parser.add_argument('inputincur', default='USD')
parser.add_argument('outcur', default='UAH')
parser.add_argument('amcur', default=100)
parser.add_argument('--start_date', default=str(datetime.now().date()))
args = parser.parse_args()
argsdict = vars(args)
incur = argsdict['inputincur']
outcur = argsdict['outcur']
amcur = argsdict['amcur']
input_date = argsdict['--start_date']
start_date = datetime.strptime(input_date, '%Y-%m-%d')
today_date = datetime.now()
finlist = list()
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
    finlist.append(['date', 'from', 'to', 'rate ', 'result'])
    for date in daylist:
        pars = {'from': incur, 'to': outcur, 'amount': amcur, 'date': date}
        response = requests.get(url, params=pars)
        data = response.json()
        finlist.append([data['date'], incur, outcur, amcur, data['info']['rate'], data['result']])


if __name__ == "__main__":
    checkdate(), make_daylist(), getresponse()
    print(finlist)
