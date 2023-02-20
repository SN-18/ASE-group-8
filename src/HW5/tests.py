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
from tables import *
from data_loader import *
from globals import the as the
import globals
from data_loader import DATA

egs = {}


def eg(key, string, fun, help):
    egs[key] = fun
    help = help + " -g " + str(key) + "\t" + str(string) + "\n"


def the_test_1():
    print(the)

def sym_test_3():
    sym = SYM(0,"")
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == round_n(sym.div())


def num_test_4():
    num = NUM(at=0,txt="")
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == round_n(num.div())


def fun(t,n=0):
    n = n + len(t)


def csv_5():
    loaded_table=csv(the['file'], fun)
    return len(loaded_table)==3192


def data_test_6():
    data = DATA(the['file'])
    col = data.cols.x[0]
    print(col.lo,col.hi,col.mid(),col.div())
    print(data.stats('mid',data.cols.y,2))

def stats_7():
    data = DATA(the['file'])
    d = {'y': data.cols.y, 'x': data.cols.x}
    for k, cols in d.items():
        print(k + 'mid'+ str(data.stats('mid', cols, 2)))
        print(''+ 'div' +str(data.stats('div', cols, 2)))



def clone_test_8():
    data1 = DATA(the['file'])
    data2 = data1.clone(data1.rows)
    print(data1.stats('mid',data1.cols.y, 2))
    print(data2.stats('mid',data2.cols.y, 2))

def around_test_9():
    data = DATA(the['file'])
    print(0,"\t    ",0,end=" \t\t")
    for k,v in data.rows[1].cells.items():
        print(v,end=" ")
    print("")
    for n, t in data.around(data.rows[1]).items():
        if n % 50 == 0:
            if n == 0:
                print(n,"    ",round_n(t['dist'], 2),"  ", sep="    " ,end = " ")
            elif n//10<10:
                print(n,"   ",round_n(t['dist'], 2),"  ", sep="    " ,end = " ")
            else:    
                print(n,"  ",round_n(t['dist'], 2),"  ", sep="    " ,end = " ")    
            for k, v in t['row'].cells.items():
                print(v, end = " ")
            print("")



def half_test_10():
    data = DATA(the['file'])
    left, right, A, B, c = data.half()
    print(len(left),len(right))
    l, r = data.clone(left), data.clone(right)
    print("l",l.stats('mid', l.cols.y, 2))
    print("r",r.stats('mid', r.cols.y, 2))

def cluster_test_11():
    data = DATA(the['file'])
    show(data.cluster(),'mid',data.cols.y,1)

def optimize_test_12():
    data = DATA(the['file'])
    show(data.sway(),'mid',data.cols.y,1)

def copy_test_13():
    t1 = dict()
    t1['a'] = 1
    t1['b'] = dict()
    t1['b']['c'] = 2
    t1['b']['d'] = [3]
    t2 = copy_t(t1)
    t2['b']['d'][0] = 10000
    print("b4",t1,"\nafter",t2)

def repcols_test_14():
    temp = dofile(the['file'])
    t_dict = dict()
    for k,v in enumerate(temp['cols']):
        t_dict[k] = v
    t = repCols(t_dict, DATA)
    map_co(t.cols.all, oo)
    map_co(t.rows, oo)

def synonyms_test_15():
    temp = dofile(the['file'])
    t_dict = dict()
    for k,v in enumerate(temp['cols']):
        t_dict[k] = v
    t = repCols(t_dict, DATA)
    d = DATA(the['file'])
    dc = t.cluster()
    show(t.cluster(), 'mid', d.cols.all, 1)

def reprows_test_16():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    map_co(rows.cols.all, oo)
    map_co(rows.rows, oo)

def prototypes_test_17():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    show(rows.cluster(), 'mid', rows.cols.all, 1)

def position_test_18():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    rows.cluster()
    repPlace(rows)

def every_test_19():
    repgrid(the['file'], DATA)

def rand_test_20():
    Seed = 1
    t = {}
    for i in range(1, 10**3):
        Seed, t[len(t)] = rint(100, None, Seed)
    Seed = 1
    u = {}
    for i in range(1, 10**3):
        Seed, u[len(u)] = rint(100, None, Seed)
    for k,v in t.items():
        assert(v == u[k])

def some_test_21():
    the['Max'] = 32
    num1 = NUM(0, "")
    for i in range(1, 10000 + 1):
        num1.add(i)
    print(num1.has)

def nums_test_22():
    num1, num2 = NUM(0, ""), NUM(0, "")
    Seed = the['seed']
    for i in range(1, 10**3):
        Seed, temp = rand_fltpy(None, None, Seed)
        num1.add(temp)
    for i in range(1, 10**3):
        Seed, temp = rand_fltpy(None, None, Seed)
        num2.add(temp**2)
    print(1,round_n(num1.mid()), round_n(num1.div()))
    print(2,round_n(num2.mid()), round_n(num2.div()))
    return 0.5 == round_n(num1.mid(), 1) and num1.mid() > num2.mid()

def cliffs_test_23():
    temp1 = {0: 8, 1: 7, 2: 6, 3: 2, 4: 5, 5: 8, 6: 7, 7: 3}
    temp2 = {0: 9, 1: 9, 2: 7, 3: 8, 4: 10, 5: 9, 6: 6}
    assert(False == cliffsDelta(temp1, temp1),"1")
    assert(True == cliffsDelta(temp1, temp2),"2")
    t1, t2 = {}, {}
    Seed = the['seed']
    for i in range(1, 10**3):
        Seed, temp = rand_fltpy(None, None, Seed)
        t1[len(t1)] = temp
    Seed = the['seed']
    for i in range(1, 10**3):
        Seed, temp = rand_fltpy(None, None, Seed)
        t2[len(t2)] = temp**0.5
    assert(False == cliffsDelta(t1, t2),"3")
    assert(True == cliffsDelta(t1, t2),"4")
    diff, j = False, 1.0
    def fun(x):
        return x * j
    while not diff:
        t3 = map_co(t1, fun)
        diff = cliffsDelta(t1, t3)
        print(">",round_n(j),diff)
        j = j * 1.025

def dist_test_24():
    data = DATA(the['file'])
    num = NUM(0, "")
    for _,row in data.rows.items():
        num.add(data.dist(row, data.rows[0]))
    print({'lo': num.lo, 'hi': num.hi, 'mid': round_n(num.mid()), 'div': round_n(num.div())})

def tree_test_25():
    data = DATA(the['file'])
    showTree(data.tree())

def sway_test_26():
    data = DATA(the['file'])
    best, rest = data.sway()
    print("\nall ",data.stats('mid',data.cols.y, 2))
    print("    ",data.stats('div',data.cols.y, 2))
    print("\nbest ",best.stats('mid',best.cols.y, 2))
    print("    ",best.stats('div',best.cols.y, 2))
    print("\nrest ",rest.stats('mid',rest.cols.y, 2))
    print("    ",rest.stats('div',rest.cols.y, 2))
    print("\nall ~= best?",diffs(best.cols.y, data.cols.y))
    print("best ~= rest?",diffs(best.cols.y, rest.cols.y))

def bins_test_27():
    data = DATA(the['file'])
    best, rest = data.sway()
    data.sway()
    temp = {'best': len(best.rows), 'rest': len(rest.rows)}
    print("all","","","",temp)
    temp = {'best': best.rows, 'rest': rest.rows}
    temp_bin = bins(data.cols.x, temp)
    for k,t in temp_bin.items():
        for _,range in t.items():
            if range['txt'] != globals.b4.values():
                print("")
            globals.b4[len(globals.b4)] = range['txt']
            print(range['txt'],range['lo'],range['hi'],round_n(value(range['y'].has, len(best.rows), len(rest.rows), 'best')), range['y'].has)
