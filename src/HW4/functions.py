import copy
import json
from operator import itemgetter
import re
import math
from globals import the as the
import globals
# from data_loader import DATA
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
    # print("printing node in cluster",node)
    if node:
        print("|.. "*lvl,end="")
        if not node['left']:
            l1 = node['data'].rows[list(node['data'].rows)[-1]]
            l2 = l1.cells[list(l1.cells)[-1]]
            print(l2)
            # print(node['data'].stats('mid', node['data'].cols.y, nPlaces))
        else:
            print(int(round_n(100 * node['c'], 0)))
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
        v = fun(k, v)
        if not u:
            l = 0
        else:
            l = len(u)
        u[l] = v
    return u


def sort_co(t, fun):
    # dict(sorted(t.items(), key=lambda a, b: a['dist'] < b['dist']))
    return dict(sorted(t.items(), key=lambda x: x[1][fun]))


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

def transpose(t):
    u = dict()
    for i in range(len(t[1])):
        u[i] = dict()
        for j in range(len(t)):
            u[i][j] = t[j][i]
    return u
    
def copy_t(t):
    return  copy.deepcopy(t)

def list_to_dict(cols):
    for k, v in cols.items():
        cols_dict = dict()
        for x, y in enumerate(v):
            cols_dict[x] = y
        cols[k] = cols_dict
    return cols

def repCols(cols, DATA):
    cols = copy_t(cols)
    # print("printing cols in repCols",cols)
    for _, col in cols.items():
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
        for j in range(1, len(col)):
            col[j - 1] = col[j]
        col.pop()
    cols = list_to_dict(cols)
    def fun(k, v):
        return "Num" + str(k)
    t_dict = dict()
    t_dict[0] = kap_co(cols[0], fun)
    t_d = dict()
    for k, v in cols.items():
        t_d[k + 1] = v
    cols = {**t_dict, **t_d}
    cols[0][len(cols[0]) - 1] = "thingsX"
    # print("printing cols in repCols",cols)
    return DATA(cols)

def repRows(t, DATA, rows=None, u=None):
    rows = copy_t(rows)
    # print("printing rows in repRows",rows)
    for j, s in rows[list(rows)[-1]].items():
        rows[0][j] = rows[0][j] + ":" + s
    rows.popitem()
    # print("printing rows in repRows",rows)
    for n, row in rows.items():
        if n == 0:
            row[len(row)] = "thingX"
        else:
            u = t['rows'][- n]
            row[len(row)] = u[len(u) - 1]
    d = DATA(rows)
    return d

def last(t):
    return t[len(t) - 1]

def repPlace(data):
    n, g = 20, dict()
    for i in range(n):
        g[i] = dict()
        for j in range(n):
            g[i][j] = " "
    maxy = 0
    print("")
    for r, row in data.rows.items():
        c = chr(97 + r).upper()
        print(c,row.cells[list(row.cells)[-1]])
        x, y = (row.x * n) // 1, (row.y * n) // 1
        maxy = int(max(maxy, y+1))
        g[y + 1][x + 1] = c
    print("")
    for y in range(maxy):
        print(" ".join(g[y].values()))

def dofile(sFile):
    file = open(sFile, 'r', encoding='utf-8')
    text  = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
    file.close()
    return json.loads(re.sub("(\w+):", r'"\1":', text))

def repgrid(sFile, DATA):
    t = dofile(sFile)
    rows = repRows(t, DATA, transpose(t['cols']))
    
    t_cols = dict()
    for k,v in enumerate(t['cols']):
        t_cols[k] = v

    cols = repCols(t_cols, DATA)
    show(rows.cluster(), "mid", rows.cols.all, 1)
    show(cols.cluster(), "mid", cols.cols.all, 1)
    repPlace(rows)

def oo(t):
    d = t.__dict__
    if t.__class__.__name__ == 'ROW':
        temp = []
        for k,v in d['cells'].items():
            temp.append(v)
        d['cells'] = temp
        temp =[]
        for k, v in d['t'].items():
            temp.append(v)
        d['t'] = temp
    d['a'] = t.__class__.__name__
    d['id'] = id(t)
    d = dict(sorted(d.items()))
    print(d)