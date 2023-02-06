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
from data_loader import DATA

egs = {}


def eg(key, string, fun, help):
    egs[key] = fun
    help = help + " -g " + str(key) + "\t" + str(string) + "\n"


def the_test_1():
    print(the)



def sym_test_3():
    sym = SYM(at=0,txt="")
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
    return len(loaded_table)==8*399

def data_6():
    data=DATA(the['file'])
    return len(data.rows)==398 and \
    data.cols.x[1].at==1 and \
    data.cols.y[0].w == -1 and \
    len(data.cols.x)==4

def stats_7():
    data = DATA(the['file'])
    d = {'y': data.cols.y, 'x': data.cols.x}
    for k, cols in d.items():
        print(k + 'mid'+ str(data.stats('mid', cols, 2)))
        print(''+ 'div' +str(data.stats('div', cols, 2)))

def clone_test_8():
    data1 = DATA(the['file'])
    # print("printing data1.rows in clone_test_8",data1.cols.names)
    # print("DATA 2")
    data2 = data1.clone(data1.rows)
    # print('len(data1.rows) =',len(data1.rows),'len(data2.rows) =',len(data2.rows))
    return len(data1.rows) == len(data2.rows) and \
        data1.cols.y[0].w == data2.cols.y[0].w and \
        data1.cols.x[1].at == data2.cols.x[1].at and \
        len(data1.cols.x) == len(data2.cols.x)

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
    left, right, A, B, mid, c = data.half()
    print(len(left),len(right),len(data.rows))
    print(A.cells,c)
    print(mid.cells)
    print(B.cells)

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
    # print("printing t.cols.all in synonyms_test_15",t.cols.all)
    # print("printing t.rows in synonyms_test_15",t.rows)
    d = DATA(the['file'])
    dc = t.cluster()
    # print("printing dc in test_synonyms()",dc)
    # print("printing temp.rows in test_synonyms()",t.rows)
    # print("printing temp.cols.all in test_synonyms()",t.cols.all)
    show(t.cluster(), 'mid', d.cols.all, 1)

def reprows_test_16():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    # print(rows.cols.all)
    # print(rows.rows)
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