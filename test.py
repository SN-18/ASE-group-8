the, help = {}, '''   
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
'''

from globals import the as the

from parser_engine import *
from functions import *
from test import *
from symbols import *

egs = {}
def eg(key, string, fun, help):
    egs[key] = fun
    help = help + " -g " + str(key) + "\t" + str(string) + "\n"


def the_test_1():
    print(the)
    # print(the.__repr__())


def rand_test_2():
    num1, num2 = NUM(), NUM()
    # print("I'm printing 'the' dict now:\n")

    seed = the['seed']

    for i in range(1, 10 ** 3):
        seed, r = rand_fltpy(0, 1, seed)
        num1.add(r)
        # num1.add(rand_fltpy(0, 1,seed))
    # print("End of first for loop in rand_test_2()")
    seed = the['seed']

    for i in range(1, 10 ** 3):
        seed, r = rand_fltpy(0,1,seed)
        num2.add(r)

    m1, m2 = round_n(num1.mid(), 10), round_n(num2.mid(), 10)

    # print("m1 is :",m1)
    # print("m2 is :",m2)


    return m1 == m2 and .5 == round_n(m1, 1)


def sym_test_3():
    sym = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == round_n(sym.div())


def num_test_4():
    num = NUM()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == round_n(num.div())