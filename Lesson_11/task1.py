import argparse


def count():
    x = int(argsvars['win']) * 3 + int(argsvars['lose'])
    return x


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="currency_checker")
    parser.add_argument('win')
    parser.add_argument('draw')
    parser.add_argument('lose')
    argsvars = vars(parser.parse_args())
    print(argsvars)
    print('count points:', count())

# TODO  найти инфу о феномене 'winwindraw'
