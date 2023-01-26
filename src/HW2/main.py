import sys
import math
import data_loader

from functions import *
from settings import *
from tests import *
from tables import *
from globals import the as the
from globals import help as help

import re
import os





def driver(options, help, funs):
    saved, fails = {}, 0
    d=cli(settings(help))

    for key in d:
        val=d[key]
        options[key]=val


    saved = options

    if options['help'] is not False:

        print(help)
    else:
        for what, fun in funs.items():
            if options['go'] == 'all' or what == options['go']:

                for k, v in saved.items():
                    options[k] = v
                Seed = options['seed']
                if funs[what]() == False:
                    fails = fails + 1

                    print(str(u'\u274C') + " fail: " + str(what))

                else:

                    print(str(u'\u2705') + " pass: " + str(what))

    sys.exit(fails)












#Main
if __name__ == '__main__':

    eg('the', 'show settings', the_test_1, help)
    eg('sym', 'check syms', sym_test_3, help)
    eg('num', 'check nums', num_test_4, help)
    eg('csv', 'read from csv', csv_5, help)
    eg('data', 'read data csv', data_6, help)
    eg("stats", "stats from data", stats_7, help)








    driver(the, help, egs)




