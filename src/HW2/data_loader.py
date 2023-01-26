#csv load
from functions import *
from tables import *

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
            map_co(src or d,fun)

    def add(self,t):
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

    def clone(self, init_para=0):
        data=DATA({self.cols.names})
        d={}
        map_co(init_para or d,lambda x:data.add(x))
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