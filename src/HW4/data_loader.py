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
        # print(s)
        if s:

            # regex="([^,]+)"
            # mo=re.search(regex,s)
            # print("current mo is printed here",mo)

            # t=dict()
            temp = dict()
            for s1 in s.split(','):
                if not t:
                    l = 0
                else:
                    l = len(t)
                t[l]=coerce(s1)
                # index2 = len(temp) + 1
                if not temp:
                    l = 0
                else:
                    l = len(temp)
                temp[l] = coerce(s1)
            fun(temp)
            # print(t)

        else:
            break


    # print(t)
    return t



#Data Class
class DATA:
    index=0
    def __init__(self,src):
        self.rows=dict()
        self.cols=None

        #for the function called fun
        def fun(x):
            self.add(x)


        if type(src) is str:
            csv(src, fun)

        else:
            d=dict()
            # print("printing src inside DATA.__init__",src)
            # print("src or d",src or d)
            for k,v in src.items():
                self.add(v)

    def add(self,t):
        # print("printing t in DATA.add",t)
        # print("printing t in data.add",t)
        if self.cols:
            t = ROW(t) if type(t) == dict else t

            if not self.rows:
                l = 0
            else:
                l = len(self.rows)
            self.rows[l]=t
            # DATA.index=DATA.index + 1
            # if COLS.index==t.len_row():
            #     COLS.index=0
            self.cols.add(t)
        else:
            self.cols=COLS(t)

    def clone(self, init_para=None):
        # print("printing self.cols.names in clone ",self.cols.names,"and its type of self.cols is ",type(self.cols))
        # print("printing self.cols.names in data1.clone",self.cols.names)
        t = {0: self.cols.names}
        data=DATA(t)
        # print("data is of type",type(data))
        d={}
        def fun(x):
            data.add(x)
        # map_co(init_para or d,fun)
        # print("printing init_para[0].cells in data1.clone",init_para[0].cells)
        # temp = dict(map(data.add, init_para.values()))
        for k, v in init_para.items():
            data.add(v)
        # lambda x:data.add(x)
        # print("printing clone of data.rows from data.cluster",data.rows)
        return data

    def stats(self,what, cols, nPlaces):
        def fun(k,col):
            if what=="div":
                # print("I'm printing col.div() inside of stats function")
                # print(col.div())
                val=col.rnd(col.div(), nPlaces)

            elif what=="mid":
                # print("I'm printing col.mid() inside of mid ")
                # print(col.mid())
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
    
    def dist(self, row1, row2, cols=None):
        # print("printing row2 in dist",row2)
        n, d = 0, 0
        if not cols:
            c = self.cols.x
        else:
            c = cols
        for _, col in c.items():
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**the['p']
        return (d / n)**(1 / the['p'])
    
    def around(self, row1, rows=None, cols=None):
        def fun(row2):
            # print("printing row2 in around->fun",row2)
            d = {'row': row2, 'dist': self.dist(row1, row2, cols)}
            return d
        # temp = map_co(rows or self.rows, fun)
        # print("printing temp in data.around",temp)
        temp = sort_co(map_co(rows or self.rows, fun), 'dist')
        # print("printing temp in around",temp)
        return temp
    
    def half(self, rows = None, cols = None, above = None):
        # print("printing rows in data.half",rows)
        c = None
        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        rows = rows or self.rows
        # print("printing rows in data.half",rows)
        # some = many(rows, the['Sample'])
        # print("printing some in data.half",some)
        A = above or any(rows)
        # print("printing A in data.half",A)
        temp = self.furthest(A, rows)
        # print("printing temp in data.half",temp)
        B = temp['row']
        # print("printing B in data.half",B)
        c = dist(A, B)
        # print("printing c in data.half",c)
        left, right = {}, {}

        def project(row):
            # print("priting row in project",row)
            x, y = cosine(dist(row, A), dist(row, B), c)
            try:
                row.x = row.x
                row.y = row.y
                # print("printing row.x in try of project",row.x)
            except:
                row.x = x
                row.y = y
                # print("printing row.x in except of project",row.x)
            d = {'row': row, 'x': x, 'y': y}
            return d
        sample = map_co(rows, project)
        # print("sample BEFORE sorting ==>",sample)
        sample = sort_co(map_co(rows, project), 'x')
        # print("sample AFTER sorting ==>",sample)
        # print("printing len(rows)//2 in data.half",len(rows)//2)
        # mid = None
        for n, tmp in sample.items():
            # n = n + 1
            if n < len(rows)//2:
                if not left:
                    l = 0
                else:
                    l = len(left)
                left[l] = tmp['row']
                mid = tmp['row']
            else:
                # print("printing index for right",)
                if not right:
                    l = 0
                else:
                    l = len(right)
                right[l] = tmp['row']
        # print("printing left, right, A, B, mid, c in data.half",left, right, A, B, mid, c)
        return left, right, A, B, mid, c
    
    def cluster(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        # print("printing rows in data.cluster",rows)
        # min = min or len(rows)**the['min']
        cols = cols or self.cols.x
        # print("printing cols in data.cluster",cols)
        # for k, v in self.cols.x.items():
        #     print("x.Row =",v.txt)
        node = {'data': self.clone(rows), 'left': None, 'right': None}
        # print("printing node.rows in data.cluster",node['data'].rows)
        if len(rows) >= 2:
            left, right, node['A'], node['B'], node['mid'], node['c'] = self.half(rows, cols, above)
            # print("printing left in data.cluster",left)
            node['left'] = self.cluster(left, min, cols, node['A'])
            node['right'] = self.cluster(right, min, cols, node['B'])
        # print("printing rows in data.cluster",rows)
        # print("----------------------------------------------")
        # print("printing node['left'] in data.cluster",node['left'])
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        return node
    
    def sway(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows)**the['min']
        cols = cols or self.cols.x
        node = {'data': self.clone(rows), 'left': None, 'right': None}
        if len(rows) > 2*min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            if self.better(node['B'], node['A']):
                left, right, node['A'], node['B'] = right, left, node['B'], node['A']
            node['left'] = self.sway(left, min, cols, node['A'])
        return node

    def furthest(self, row1, rows=None, cols=None):
        t = self.around(row1, rows, cols)
        last_key = list(t)[-1]
        return t[last_key]