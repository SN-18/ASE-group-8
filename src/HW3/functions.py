import re
import math
seed = 937162211
#miscelleneous functions
def rand_intpy(lo, hi):
    return math.floor(0.5 + rand_fltpy(lo, hi))


def rand_fltpy(lo, hi, seed):
    # print("I am printing seed inside rand_flty",seed)
    lo, hi = lo or 0, hi or 1
    # print("I am printing seed and type of seed, should be a list",seed,type(seed))
    seed = (16807 * seed) % 2147483647
    return seed, lo + (hi - lo) * seed / 2147483647


def round_n(n, nPlaces=3):
    multiplier = 10 ** (nPlaces)
    return math.floor(n*multiplier+ 0.5)/multiplier
# List functions
# map collection
def map_co(t, fun):
    u = {}
    for k, v in t.items():
        v, k = fun(v)
        u[k or (1 + len(u))] = v
    return u


def kap_co(t, fun):
    u = {}
    for k, v in t.items():
        v, k = fun(k, v)
        u[k or 1 + (1 + len(u))] = v
    return u


def sort_co(t, fun):
    dict(t.values().sort(key=fun))
    return t


def keys_co(t):
    return sorted(t.keys())




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

def concat(table, sep):
    ret = ""
    if table:
        first = True
        for _, v in table:
            if first:
                ret = ret + v
                first = False
                break
            ret = ret + sep + v
    return ret


def show(node, what, cols, nPlaces, lvl):
    if node:
        lvl = lvl or 0
        print(("| "*lvl) + len(node.data.rows) + "  ")
        show(node.left, what, cols, nPlaces, lvl+1)
        show(node.right, what, cols, nPlaces, lvl+1)

def o(t, isKeys=False, fun=0):
    if type(t) is not "table":
        return str(t)
    def func(k, v):
        if not v.find("^_"):
            return ":%s %s".format(o(k), o(v))
    fun = func
    return "{" + concat(len(t)>0 and not isKeys and map_co(t, o) or sort_co(kap_co(t, fun)), " ") + "}"
