# from datetime import timedelta, datetime
# today_date = datetime.now()
# start_date = datetime.strptime(input_date,'%Y-%m-%d')
#
# while start_date < today_date:
#     print(start_date.date())
#     start_date += timedelta(1)
#
# import argparse
#
# parser = argparse.ArgumentParser(description="currency_checker")
# parser.add_argument()
# inputed = parser.parce_args()
# print(inputed)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="currency_checker")
    parser.add_argument('inputincur')
    parser.add_argument('outcur')
    parser.add_argument('amcur')
    args = parser.parse_args()
    argsdict = vars(args)

    print(type(argsdict['inputincur']))
    # print(type(vars(some)))
    # print(some_l['input'])


