#csv load
from operator import itemgetter
from functions import *
from tables import *
from functions import *
from globals import the as the
from globals import help as help

def csv(sFilename,fun):
    filename=open(sFilename)
    src=filename
    s=t=None
    t = dict()
    while True:
        s=src.readline()
        if s:
            temp = dict()
            for s1 in s.split(','):
                if not t:
                    l = 0
                else:
                    l = len(t)
                t[l]=coerce(s1)
                if not temp:
                    l = 0
                else:
                    l = len(temp)
                temp[l] = coerce(s1)
            fun(temp)

        else:
            break
    return t



#Data Class
class DATA:
    index=0
    def __init__(self,src):
        self.rows=dict()
        self.cols=None
        def fun(x):
            self.add(x)
        if type(src) is str:
            csv(src, fun)
        else:
            d=dict()

            for k,v in src.items():
                self.add(v)

    def add(self,t):
        if self.cols:
            t = ROW(t) if type(t) == dict else t

            if not self.rows:
                l = 0
            else:
                l = len(self.rows)
            self.rows[l]=t

            self.cols.add(t)
        else:
            self.cols=COLS(t)

    def clone(self, init_para=None):

        t = {0: self.cols.names}
        data=DATA(t)
        d={}
        def fun(x):
            data.add(x)

        for k, v in init_para.items():
            data.add(v)

        return data

    def stats(self,what, cols, nPlaces):
        def fun(k,col):
            if what=="div":

                val=col.rnd(col.div(), nPlaces)

            elif what=="mid":

                val=col.rnd(col.mid(), nPlaces)

            return val,col.txt
        return kap_co(cols or self.cols.y,fun)

    def better(self, row1, row2):
        s1, s2, ys, x, y = 0, 0, self.cols.y, None, None
        for _, col in ys.items():
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.e ** (col.w * (x - y)/len(ys))
            s2 = s2 - math.e ** (col.w * (y - x)/len(ys))
        return s1/len(ys) < s2/len(ys)
    
    def betters(self, n=None):
        def fun(r1, r2):
            return self.better(r1, r2)
        tmp = sort_co(self.rows, fun)
        return n and slice(tmp, 1, n), slice(tmp, n+1) or tmp
    
    # def dist(self, row1, row2, cols=None):

    #     n, d = 0, 0
    #     if not cols:
    #         c = self.cols.x
    #     else:
    #         c = cols
    #     for _, col in c.items():
    #         n = n + 1
    #         d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**the['p']
    #     return (d / n)**(1 / the['p'])

    def dist(self, t1, t2, cols=None):
        def sym(x, y):
            return x == y and 0 or 1
        def num(x, y):
            if x == '?':
                x = y<0.5 and 1 or 1
            if y == '?':
                y = x<0.5 and 1 or 1
            return abs(x - y)
        def dist1(col, x, y):
            if x=='?' and y=='?':
                return 1
            if isinstance(col, SYM):
                return sym(x, y)
            else:
                num(col.norm(x), col.norm(y))
        d, cols = 0, (cols or self.cols.x)
        for _, col in cols.items():
            # d = d + dist1(col, t1[col.at], t2[col.at])**the['p']
            d = d + col.dist(t1.cells[col.at], t2.cells[col.at])**the['p']
        return (d / len(cols))**(1 / the['p'])
    
    def around(self, row1, rows=None, cols=None):
        def fun(row2):

            d = {'row': row2, 'dist': self.dist(row1, row2, cols)}
            return d

        temp = sort_co(map_co(rows or self.rows, fun), 'dist')

        return temp
    
    def half(self, rows = None, cols = None, above = None):
        c = None
        def dist(row1, row2):
            return self.dist(row1, row2, cols)
        def cos(a, b, c):
            return (a**2 + c**2 - b**2) / (2*c)

        rows = rows or self.rows

        some = many(rows, the['Halves'])

        A = above or any(some)
        temp = self.furthest(A, rows)
        B = temp['row']
        c = temp['dist']
        left, right, eval = {}, {}, None

        def project(row):

            d = {'row': row, 'x': cos(dist(row, A), dist(row, B), c)}
            return d

        sample = sort_co(map_co(rows, project), 'x')

        for n, tmp in sample.items():
            if n < len(rows)//2:
                if not left:
                    l = 0
                else:
                    l = len(left)
                left[l] = tmp['row']
                mid = tmp['row']
            else:
                if not right:
                    l = 0
                else:
                    l = len(right)
                right[l] = tmp['row']
        if the['Reuse'] and above:
            evals = 1
        else:
            evals = 2
        return left, right, A, B, c, evals
    
    def cluster(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows)**the['min']
        cols = cols or self.cols.x
        node = {'data': self.clone(rows), 'left': None, 'right': None}
        if len(rows) >= 2*min:
            left, right, node['A'], node['B'], c, evals = self.half(rows, cols, above)
            # print("printing left in data.cluster",left)
            node['left'] = self.cluster(left, min, cols, node['A'])
            node['right'] = self.cluster(right, min, cols, node['B'])
        return node
    


    def sway(self):
        def worker(rows, worse, evals0=None, above=None):
            if len(rows) <= len(self.rows)**the['min']:
                many_var=many(worse, the['rest']*len(rows))
                return rows, many_var, evals0

            else:
                l, r, A, B, c, evals = self.half(rows, None, above)
                if self.better(B, A):
                    l, r, A, B = r, l, B, A

                for _,row in r.items():
                    worse[len(worse)] = row
                # first,second=worker(l,worse, evals+evals0, A)
                # return first,second
                return worker(l,worse, evals+evals0, A)

        best, rest, evals = worker(self.rows, {}, 0)
        return self.clone(best), self.clone(rest), evals

    def furthest(self, row1, rows=None, cols=None):
        t = self.around(row1, rows, cols)
        far = math.floor(len(t)*the['Far'])
        last_key = list(t)[far]
        return t[last_key]

    def tree(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows)**the['min']
        cols = cols or self.cols.x
        node = {'data': self.clone(rows), 'left': None, 'right': None}
        if len(rows) >= 2*min:
            left, right, node['A'], node['B'], c, evals = self.half(rows, cols, above)
            node['left'] = self.cluster(left, min, cols, node['A'])
            node['right'] = self.cluster(right, min, cols, node['B'])
        return node
    
    def xpln(self, best, rest):
        def v(has):
            return value(has, len(best.rows), len(rest.rows), "best")
        def score(ranges):
            rule = RULE(ranges, maxSizes)
            if rule:
                print(showRule(rule))
                bestr = selects(rule, best.rows)
                restr = selects(rule, rest.rows)
                if len(bestr) + len(restr) > 0:
                    return v({'best': len(bestr), 'rest': len(restr)}), rule
        tmp, maxSizes = {}, {}
        for _, ranges in bins(self.cols.x, {'best': best.rows, 'rest': rest.rows}).items():
            # print("printing ranges in DATA xpln",ranges)
            maxSizes[ranges[1].txt] = len(ranges)
            print("")
            for _, range in ranges.items():
                print(range.txt, range.lo, range.hi)
                tmp[len(tmp)] = {'range': range, 'max': len(ranges), 'val': v(range.y.has)}
        rule, most = firstN(sort_co(tmp, 'val'), score)
        return rule, most