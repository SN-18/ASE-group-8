from operator import itemgetter
import re
import math
from globals import the as the
import globals
# global seed
# seed = 937162211
#miscelleneous functions
def rand_intpy(lo, hi):
    globals.seed, val = rand_fltpy(lo, hi, globals.seed)
    # print("printing val in rand_intpy",val)
    return math.floor(0.5 + val)


def rand_fltpy(lo, hi, seed):
    # print("I am printing seed inside rand_flty",seed)
    lo, hi = lo or 0, hi or 1
    # print("I am printing seed and type of seed, should be a list",seed,type(seed))
    seed = (16807 * seed) % 2147483647
    return seed, lo + (hi - lo) * seed / 2147483647


def round_n(n, nPlaces=3):
    multiplier = 10 ** (nPlaces)
    return math.floor(n*multiplier+ 0.5)/multiplier

def cosine(a, b, c):
    x1 = (a**2 + c**2 - b**2) / (2*c)
    x2 = max(0, min(1, x1))
    y = (a**2 - x2**2)**0.5
    return x2, y

def show(node, what, cols, nPlaces, lvl = 0):
    if node:
        lvl = lvl or 0
        print("| "*lvl,len(node['data'].rows)," ",end=" ")
        if not node['left'] or lvl == 0:
            print(node['data'].stats('mid', node['data'].cols.y, nPlaces))
        else:
            print(" ")
        show(node['left'],what,cols,nPlaces,lvl + 1)
        show(node['right'],what,cols,nPlaces,lvl + 1)

# List functions
# map collection
def map_co(t, fun):
    u = {}
    for k, v in t.items():
        # print("printing k and v in map_co",k,v)
        v = fun(v)
        if not u:
            l = 0
        else:
            l = len(u)
        u[l] = v
    # print("printing u in map_co",u)
    return u


def kap_co(t, fun):
    u = {}
    for k, v in t.items():
        v, k = fun(k, v)
        u[k or 1 + (1 + len(u))] = v
    return u


def sort_co(t, fun):
    # dict(sorted(t.items(), key=lambda a, b: a['dist'] < b['dist']))
    return dict(sorted(t.items(), key=lambda x: x[1]['dist']))


def keys_co(t):
    return sorted(t.keys())

def lt(x):
    def fun(a, b):
        return a[x] < b[x]
    return fun

def any(t):
    # print("printing len(t) in any",len(t))
    ind = rand_intpy(0, len(t) - 1)
    # if ind == 398:
    #     ind = 397
    return t[ind]

def many(t, n):
    u = dict()
    for i in  range(n):
        if not u:
            l = 0
        else:
            l = len(u)
        u[l] = any(t)
    return u



def coerce(s):
    # inner function

    if s == 'true':
        return True
    elif s == 'false':
        return False
    else:
        try:
            s_ret = int(s)
            return s_ret
        except ValueError:
            try:
                s_ret = float(s)
                return s_ret
            except ValueError:
                try:
                    regex = re.compile('(^\s*)(.+?)(\s*$)')
                    mo = regex.search(s)
                    return mo.group(2)
                except:
                    return s

    def rnd(x, n):
        return x
