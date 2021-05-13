import argparse

parser = argparse.ArgumentParser(description="currency_checker")
parser.add_argument('old')
parser.add_argument('new')
parser.add_argument('count')
parser.add_argument('--string')
argsvars = vars(parser.parse_args())


def renew_string():
    endstring = argsvars['string'].replace(argsvars['old'], argsvars['new'], argsvars['count'])
    return endstring
# print(renew_string())
