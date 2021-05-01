import getopt
import sys

import pingpong as pp
import datascience as dc


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
                dc.work()

    print('main.py -e game | work')
