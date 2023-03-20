import copy
import json
from operator import itemgetter
import os
import re
import math
from globals import the as the
import globals
from tables import *
from sys import maxsize

b4 = {}

#miscelleneous functions
def rand_intpy(lo, hi):
    globals.seed, val = rand_fltpy(lo, hi, globals.seed)

    return math.floor(0.5 + val)

def rint(lo, hi, seed):
    seed, val = rand_fltpy(lo, hi, seed)

    return seed, math.floor(0.5 + val)

def rand_fltpy(lo, hi, seed):

    lo, hi = lo or 0, hi or 1

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
    # print("debugging sort_co, this is fun:",fun)
    key=lambda x: x[1][fun]
    return dict(sorted(t.items()))


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

    for j, s in rows[list(rows)[-1]].items():
        rows[0][j] = rows[0][j] + ":" + s
    rows.popitem()

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

def add(col,x,n=0):
    if x!="?":
        n=n or 1
        col.n=col.n + n
        if isinstance(col, SYM):
            col.has[x]= n + (col.has[x] or 0)
            if col.has[x]>col.most:
                col.most,col.mode=col.has[x],x
        else:
            col.lo, col.hi=min(x,col.lo),max(x,col.hi)
            all=len(col.has)
            pos=(all<the.Max and all+1) or (rand_fltpy()< the["Max"]/col.n and rand_intpy(1,all))
            if pos:
                col.has[pos]=x 
                col.ok=False
    
def adds(self,col,t):
    for _,x in t.items():
        self.add(col,x)
    return col

def RANGE(at, txt, lo, hi=None):
    d = {'at': at, 'txt': txt, 'lo': lo, 'hi': lo or hi or lo, 'y': SYM(-1, "")}
    return d

def RULE(ranges, maxSize):
    t = {}
    for _,range in ranges.items():
        # print("this is the function RULE, and this is range dict:",range)

        range_var=range['txt'] if 'txt' in range else 0

        # 'txt' not in

        if range_var not in t:
            t[range_var] = {}

        lo_val=range['lo'] if 'lo' in range else 0
        hi_val=range['hi'] if 'hi' in range else 0
        at_val=range['at'] if 'at' in range else 0

        d = {'lo': lo_val, 'hi': hi_val, 'at': at_val}
        t[range_var] = d
    return prune(t, maxSize)

def prune(rule, maxSize):
    n = 0
    for txt, ranges in rule.items():
        n = n + 1
        if 'txt' in maxSize:
            if len(ranges) == maxSize['txt']:
                n = n + 1
                rule[txt] = None

    if n > 0:
        return rule

def extend(range, n, s):
    range['lo'] = min(n, range['lo'])
    range['hi'] = max(n, range['hi'])
    range['y'].add(s)

def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1, len(t)+1):
            t[j].lo = t[j - 1].hi
            t[0].lo = (-1)*(maxsize)
            t[len(t)].hi = maxsize
        return t
    ranges1, j, left, right, y = {}, 0, None, None, None
    # print("printiing ranges0",ranges0)
    while j < len(ranges0) - 1:
        temp1, temp2 = list(ranges0)[j], list(ranges0)[j + 1]
        left, right = ranges0[temp1], ranges0[temp2]
        if right:
            y = merge2(left['y'], right['y'])
            if y:
                j = j + 1
                left['hi'], left['y'] = right['hi'], y
        l = len(ranges1)
        ranges1[l] = left
        j = j + 1
    if len(ranges0) == len(ranges1):
        return noGaps(ranges0)
    else:
        return mergeAny(ranges1)

# def merges(ranges0, nSmall, nFar):
#     def noGaps(t):
#         # print("printing t in merges noGaps", t)
#         for j in range(1, len(t)+1):
#             t[j].lo = t[j - 1].hi
#             t[0].lo = (-1)*(maxsize)
#             t[len(t)].hi = maxsize
#         return t
#     def try2Merge(left, right, j):
#         y = merged(left['y'], right['y'], nSmall, nFar)
#         if y:
#             j = j + 1
#             left['hi'], left['y'] = right['hi'], y
#         return j, left
#     ranges1, j, here = {}, 0, None
#     # print("printiing ranges0",ranges0)
#     while j < len(ranges0) - 1:
#         here = ranges0[j]
#         if j < len(ranges0) - 1:
#             j, here = try2Merge(here, ranges0[j+1], j)
#             j = j + 1
#             ranges1[len(ranges1)] = here
#     if len(ranges0) == len(ranges1):
#         return noGaps(ranges0)
#     else:
#         return merges(ranges1, nSmall, nFar)

def merge(col1,col2):
    new_var=copy_t(col1)
    if isinstance(col1, SYM):
        for x,n in col2.has.items():
            new_var.add(n)
            # add(new_var,x,n)
    else:
        for _,n in col2.has.items():
            add(new_var,n)
        new_var.lo=min(col1.lo,col2.lo)
        new_var.hi=max(col1.hi,col2.hi)
    return new_var

    
# def merged(col1, col2, nSmall, nFar):
#     new_var = merge(col1, col2)
#     if nSmall and (col1.n < nSmall) or (col2.n < nSmall):
#         return new_var
#     if nFar and (not isinstance(col1, SYM)) and abs(col1.mid() - col2.mid()) < nFar:
#         return new_var
#     if new_var.div()<=(col1.div()*col1.n \
#     +col2.div()*col2.n)/new_var.n:
#         return new_var
    
def merge2(col1,col2,new_var=None): 
    new_var=merge(col1,col2)
    if new_var.div()<=(col1.div()*col1.n \
    +col2.div()*col2.n)/new_var.n:
        return new_var

def bin(col, x):
    if x=="?" or isinstance(col, SYM):
        return x
    tmp = (col.hi - col.lo) / (the['bins'] - 1)
    if col.hi == col.lo:
        return 1
    else:
        return math.floor(x / tmp + 0.5)*tmp

def bins(cols, rowss):
    def fun(x):
        return x

    out = dict()


    for num_object in cols.values():
        if isinstance(num_object,NUM):

            # round_n(value(range['y'].has, len(best.rows), len(rest.rows), 'best'))

            ind = rand_intpy(0, len(num_object.has) - 1)
            print(num_object.txt, num_object.hi, num_object.lo,round_n(value(num_object.has, ind, len(num_object.has))),"{'best': ",len(num_object.has),"'rest':",ind,"}")
            print("")
            # print("ind is: ",ind)


        else:
            pass


    for _, col in cols.items():
        ranges = dict()
        for y, rows in rowss.items():
            for _, row in rows.items():
                x = row.cells[col.at]
                if x != "?":
                    k = int(bin(col, x))
                    if not k in ranges:
                        ranges[k] = RANGE(col.at, col.txt, x)
                    extend(ranges[k], x, y)
                else:
                    print("x is apparently ?",x)
        ranges = sort_co(map_co(ranges, fun), "lo")

        r = None
        if isinstance(col, SYM):

            r = ranges
        else:

            r = mergeAny(ranges)
        out[len(out)] = r

    return out

# def bins(cols, rowss):
#     def fun(x):
#         return x
#     def with1Col(col):
#         n, ranges = withAllRows(col)
#         ranges = sort_co(map_co(ranges, fun),'lo')
#         if isinstance(col, SYM):
#             return ranges
#         else:
#             return merges(ranges, n/the['bins'], the['d']*col.div())
#     def withAllRows(col):
#         def xy(x, y):
#             if x != "?":
#                 k = int(bin(col, x))
#                 if not k in ranges:
#                     ranges[k] = RANGE(col.at, col.txt, x)
#                 extend(ranges[k], x, y)
#         n, ranges = 0, {}
#         for y, rows in rowss.items():
#             for _, row in rows.items():
#                 xy(row.cells[col.at], y)
#         return n, ranges
#     return map_co(cols, with1Col)

def cliffsDelta(ns1,ns2):
    if len(ns1)>256:
        ns1=many(ns1,256)
    if len(ns2)>256:
        ns2=many(ns2,256)
    
    
    if len(ns1)>10*len(ns2):
        ns1=many(ns1,10*len(ns2))
    
    if len(ns2)>10*len(ns1):
        ns2=many(ns2,10*len(ns1))

    n,gt,lt=0,0,0
    for _,x in ns1.items():
        for _,y in ns2.items():
            n=n+1
            if x>y:
                gt=gt+1
            if x<y:
                lt=lt+1
    return abs(lt-gt)/n >the['cliffs']

def diffs(nums1,nums2):
    def fun(k,nums):
        return cliffsDelta(nums.has,nums2[k].has),nums.txt
    return kap_co(nums1,fun)

def showTree(tree, lvl=None, post=None):
    if tree:
        lvl = lvl or 0
        print("|.."*lvl,"[",len(tree['data'].rows),"]",end="")
        if lvl == 0 or not tree['left']:
            print(tree['data'].stats("mid", tree['data'].cols.y, 3))
        else:
            print("")
        showTree(tree['left'], lvl + 1)
        showTree(tree['right'], lvl + 1)

    

def slice(t, go=None, stop=None, inc=None):
    if go and go < 0:
        go = len(t) + go
    if stop and stop < 0:
        stop = len(t) + stop
    u = {}
    for j in range((go or 1)//1,(stop or len(t))//1,(inc or 1)//1):
        u[len(u)] = t[j]
    return u

def say(*a):
    for item in a:
        print(item.strip(), file=sys.stderr, end=' ')

def sayln(*a):
    for item in a:
        print(item.strip(), file=sys.stderr, end=' ')
    print('\n')

def value(has, nB=None, nR=None, sGoal=None):
    sGoal, nB, nR = sGoal or True, nB or 1, nR or 1
    b, r = 0, 0
    for x,n in has.items():
        if x == sGoal:
            b = b + n
        else:
            r = r + n
    b, r = b/(nB+1/math.inf), r/(nR+1/math.inf)
    return b**(2/(b+r))

def firstN(sortedRanges, scoreFun):
    def fun(r):
        # print("r is:",r)
        print(r["range"]["txt"], r["range"]["lo"], r["range"]["hi"], round_n(r["val"]), r["range"]["y"].has)
    print("")
    # print("sortedRanges before map_co is:",sortedRanges)
    map_co(sortedRanges, fun)
    # print("sortedRanges is",sortedRanges)
    first = sortedRanges[0]["val"]
    def useful(range):
        if range["val"] > 0.5 and range["val"] > first/10:
            return range
    sortedRanges = map_co(sortedRanges, useful)
    most, out = -1, None
    for n in range(0, len(sortedRanges)):
        # print("I'm inside the for loop, testing")
        score_fun_variable=scoreFun(map_co(slice(sortedRanges, 0, n), on('range')))
        # print("this is debugging scoreFun,scoreFun is:",score_fun_variable)
        if score_fun_variable is None:
            continue
        tmp, rule = scoreFun(map_co(slice(sortedRanges, 0, n), on('range')))
        if tmp and tmp > most:
            out, most = rule, tmp
    return out, most

def showRule(rule):
    def pretty(range):
        return range.lo==range.hi and range.lo or {range.lo, range.hi}
    def merges(attr, ranges):
        return map_co(merge(sort_co(ranges, "lo")), pretty), attr
    def merge(t0):
        t, j, left, right = {}, 0, 0 , 0
        empty_dict=dict()
        while j < len(t0) - 1:

            left= t0[j] if j in t0 else empty_dict
            right=t0[j+1] if (j+1) in t0 else empty_dict


            if right and left["hi"] == right["lo"]:
                left["hi"] = right["hi"]
                j = j + 1
            t[len(t)] = {'lo': left['lo'] if 'lo' in left else 0, 'hi': left['hi'] if 'hi' in left else 0}
            j = j + 1
        if len(t0) == len(t):
            return t
        else:
            return merge(t)
    return kap_co(rule, merges)

def selects(rule, rows):
    def disjunction(ranges, row):
        empty_dict=dict()
        # print(ranges.items())
        for _, range_stat in ranges.items():
            current_range=range_stat
            # print("current range is:",current_range)
            # print("type of range_stat is:",type(range_stat))
            # print("this is range_stat, should not be an int, I suppose:", range_stat)
            # print("this is ranges.items()",ranges.items())

            if range_stat==0:
                lo=hi=at=0
            else:
                lo= range_stat["lo"] if 'lo' in range_stat else empty_dict
                hi= range_stat["hi"] if 'hi' in range_stat else empty_dict
                at= range_stat["at"] if 'lo' in range_stat else empty_dict


            # print("row is:",row)
            # print("type of row is:",type(row))

            try:
                if row['at'] == '?':
                    x = True

                if 'at' in row:
                    print("row['at'] is:",row['at'])

                x = row['at'] if 'at' in row else empty_dict

                if x == "?":
                    return True

                if lo == hi and lo == x:
                    return True

                if lo <= x and x < hi:
                    return True

            except:
                continue





            # else:
            #     if 'at' in row:
            #         print("row['at'] is:",row['at'])




        return False

    def conjunction(row):
        for _,ranges in rule.items():
            if not disjunction(ranges, row):
                return False
        return True

    def fun(r):
        if conjunction(r):
            return map_co(rows, r)
    return map_co(rows, fun)

def on(x):

    def fun(t):
        # print("t is:",t)
        empty_dict=dict()
        return t[x] if t else empty_dict
    return fun

def gaussian(mu,sd):
    pass

#dummy scottKnot
def scottKnot():
    pass

def bootstrap():
    pass

def tiles():
    pass

def mid():
    pass
def RX():
    pass
def samples():
    pass


