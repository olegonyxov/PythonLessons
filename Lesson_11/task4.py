import argparse

parser = argparse.ArgumentParser(description="string_maker")
parser.add_argument('old')
parser.add_argument('new')
parser.add_argument('count')
parser.add_argument('--string', type=str, nargs="?")
argsvars = vars(parser.parse_args())


def renew_string():
    endstring = argsvars['string'].replace(argsvars['old'], argsvars['new'], argsvars['count'])
    return endstring


print(renew_string())
