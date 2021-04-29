import argparse
from datetime import timedelta, datetime
import requests


def checkdate():
    input_date = argsdict['start_date']
    start_date = datetime.strptime(input_date, '%Y-%m-%d')
    if start_date > today_date:
        start_date = today_date
    return start_date


def make_daylist():
    tempdate = checkdate()
    while tempdate <= today_date:
        daylist.append(tempdate.date())
        tempdate += timedelta(1)


def getresponse():
    url = 'https://api.exchangerate.host/convert'
    incur = argsdict['inputincur']
    outcur = argsdict['outcur']
    amcur = argsdict['amcur']
    finlist.append(['date', 'from', 'to', 'rate ', 'result'])
    for date in daylist:
        pars = {'from': incur, 'to': outcur, 'amount': amcur, 'date': date}
        response = requests.get(url, params=pars)
        data = response.json()
        finlist.append([data['date'], incur, outcur, amcur, data['info']['rate'], data['result']])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="currency_checker")
    parser.add_argument('inputincur', default='USD')
    parser.add_argument('outcur', default='UAH')
    parser.add_argument('amcur', default=100)
    parser.add_argument('--start_date', default=str(datetime.now().date()), nargs='?')
    args = parser.parse_args()
    argsdict = vars(args)
    today_date = datetime.now()
    finlist = []
    daylist = []
    checkdate(), make_daylist(), getresponse()
    print(finlist)
