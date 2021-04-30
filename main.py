import getopt
import sys

import pingpong as pp
import pandas as pd


def work():
    print('Start Working')
    data = pd.read_csv('countries.csv', ',')
    print(data.head())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('Command Lines Arguments '+str(len(sys.argv)))

    try:
        opts, args = getopt.getopt(sys.argv[1:], "e:", ["execute"])
    except getopt.GetoptError:
        print
        'start.py -e game | work'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-e':
            if arg == 'game':
                pp.start()
            elif arg == 'work':
                work()

    print('main.py -e game | work')
