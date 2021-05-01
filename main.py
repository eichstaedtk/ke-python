import getopt
import sys

import pingpong as pp
import pandas as pd


def work():
    print('Start Working')
    data = pd.read_csv('countries.csv', ',')
    print(data.head())

    # Display some basic information as rows, columns and some basic statistical info.
    print(data.describe())

    # show the last 4 rows of the data frame.
    print(data[len(data)-4:])

    # Show all the row of countries who have the EURO
    print(data.query('Currency == "EUR"'))

    # Show only name and Currency in a new data frame
    data2 = data[["Name", "Currency"]]
    print(data2)

    # Show only the rows/countries that have more than 2000 BIP (it is in Milliarden USD Bruttoinlandsprodukt)
    print(data.query('BIP > 2000')["Name"])

    # Select all countries where with inhabitants between 50 and 150 Mio
    print(data.query('People > 50000000 and People < 150000000'))


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
