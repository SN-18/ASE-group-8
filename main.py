#contains driver code, that is code in main
#that calls all other functions.py and runs the project

import parser_engine
import symbols
import table
import functions

from globals import the as the
from globals import help as help
from parser_engine import *
from functions import *
from test import *

def driver(options, help, funs):
    # print("We have entered the driver code")
    saved, fails = {}, 0
    d=cli(settings(help))
    for key in d:
        val=d[key]
        options[key]=val

    # print("is options empty?\n")
    # print(options)
    saved = options
    # print("I am now printing options",options)
    if options['help'] is not False:
        # print("I am inside the if statement")
        print(help)
    else:
        # print("I am printing funs\n")
        # print(funs)
        # print("I am now printing fun.items",funs.items())

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
    # print("System didn't pass, raise generic exception")
    # sys.exit(fails)





if __name__ == '__main__':
    eg('the', 'show settings', the_test_1, help)
    eg('rand', 'generate, reset, regenerate same', rand_test_2, help)
    eg('sym', 'check syms', sym_test_3, help)
    eg('num', 'check nums', num_test_4, help)

    driver(the, help, egs)




