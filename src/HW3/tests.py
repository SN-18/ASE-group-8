from tables import *
from data_loader import *
from globals import the as the

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

def data_5():
    data=DATA(the['file'])
    return len(data.rows)==398 and \
    data.cols.x[1].at==1 and \
    data.cols.y[0].w == -1 and \
    len(data.cols.x)==4

def clone_6():
    data1 = DATA(the['file'])
    data2 = data1.clone(data1.rows)
    return len(data1.rows) == len(data2.rows) and \
        data1.cols.y[1].w == data2.cols.y[1].w and \
        data1.cols.y[1].at == data2.cols.y[1].at and \
        len(data1.cols.x) == len(data2.cols.x)

def around_7():
    data=DATA(the['file'])
    print(0, 0, o(data.rows[1].cells))
    for k, v in data.around(data.rows[1]):
        if k % 50 == 0:
            print(k, round_n(v.dist, 2), o(v.row.cells))

def half_8():
    data=DATA(the['file'])
    left, right, A, B, mid, c = data.half()
    print(len(left), len(right), len(data.rows))
    print(o(A.cells), c)
    print(o(mid.cells))
    print(o(B.cells))

def cluster_9():
    data=DATA(the['file'])
    show(data.cluster(), "mid", data.cols.y, 1)

def optimize_10():
    data=DATA(the['file'])
    show(data.sway(), "mid", data.cols.y, 1)
