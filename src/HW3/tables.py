import re

from functions import *

import sys

import itertools

# from tables import table as t
#NUM class
# Num class inherited from global object class
# and it's related methods implemented inside of NUM class

class obj:
    id = 0


    @classmethod
    def update(cls):
        cls.id = cls.id + 1

    def __init__(self, s: str):
        self.t_metatable = {}
        self.t = {}
        obj.update()
        obj.add_child(self, s)

# Meta table class
class table:
    def __init__(self):
        self.key = ""
        self.value = -1

class NUM():
    table = table()
    instance_id = next(itertools.count())


    def __init__(self, at, txt):
        # super.__init__(s)
        self.n = 0
        self.d=0
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = (-1) * sys.maxsize
        self.at = at if at else 0
        self.txt = txt if txt else ""
        self.w = -1 if txt.find('-') != -1 else 1

        self.count=NUM.instance_id

    # n_cur is the current n
    def add(self, n_current):
        # print("my value of n_current in NUM.add is",n_cur)
        if n_current != "?":
            n_current=float(n_current)

            # try:
            #
            #     n_current=float(n_current)
            #
            #     # n_curr=len(self.all)
            #     # print("I'm in try and n_cur is,",n_cur)
            # except:
            #     n_current=float(399)




            self.n = self.n + 1
            self.d = n_current - self.mu
            # print("my current value of d should not be 0",self.d)


            self.mu = self.mu + self.d / self.n
            # print("my value of n and mu are, resp:",self.n,self.mu)
            # print("this is the value of d",d)
            # print("I am updating mu", self.mu)
            self.m2 = self.m2 + self.d * (n_current - self.mu)
            self.lo = min(n_current, self.lo)
            self.hi = max(n_current, self.hi)

    def mid(self):
        # print("this is the value of mu inside of self.mid",self.mu)
        return self.mu

    def div(self):
        var1 = self.m2 < 0 or self.n < 2
        var2 = 0
        var3 = ((self.m2) / (self.n - 1)) ** (0.5)
        return (var1 and var2) or var3

    def rnd(self, x, n):
        if x == '?':
            return x
        else:
            # print("we are in num.rnd")
            # print(x)
            var=round_n(x,n)
            # print("var's value is:",var)
            return round_n(x, n)
    
    def norm(self, n):
        if n == "?":
            return n
        else:
            return (n - self.lo) / (self.hi - self.lo + 1e-32)

    def dist(self, n1, n2):
        if n1 == "?" and n2 == "?":
            return 1
        n1, n2 = self.norm(n1), self.norm(n2)
        if n1 == "?":
            if n2 < 0.5:
                n1 = 1
            else:
                n1 = 0
        if n2 == "?":
            if n1 < 0.5:
                n2 = 1
            else:
                n2 = 0
        return abs(n1 - n2)



class SYM():
    # has = {}
    def __init__(self,at,txt):
        # super.__init__(s)
        self.n = 0
        self.has={}
        self.most = 0
        self.mode = None
        self.at = at or 0
        self.txt = txt or ""

    # def obj_table():
    #     print(obj.t)

    def add(self, x: str):
        if x != "?":
            self.n = self.n + 1
            value = self.has.get(x, 0)
            self.has[x] = value + 1

            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        def fun(p):
            return p * (math.log(p, 2))

        # e_n is the negative entropy
        # n_cur is the current n, not the instance value self.n
        # n, here, represents frequency

        e_n = 0
        # print("I am printing self.has",self.has)

        for _,val in self.has.items():
            # print("I am printing tuples in self.has",element)
            # curr_val=self.has[element[1]]

            n_cur=val
            # print("I am printing n_cur, it should be an integer",n_cur)
            # print("I am printing has, it should contain")
            e_n = e_n + fun(n_cur / self.n)

        return (-1) * e_n
        
    def rnd(self, x, n=0):
        return x

    def dist(self, s1, s2):
        if s1 == "?" and s2 == "?":
            return 1
        else:
            if s1 == s2:
                return 0
            else:
                return 1





#row
class ROW:
    def __init__(self,t):
        self.cells=t
        self.t=t
    def len_row(self):
        return len(self.t)


class COLS:
    index1=0
    index2=0
    index3 =0

    def __init__(self,t):
        self.names=t
        self.all=dict()
        # self.index=0
        self.x=dict()
        self.y=dict()
        self.klass=None

        # print("I am printing t inside of COLS", str(t))

        for n,s in t.items():
            # print("This is the value of n,s",n,s)
            # print("this is the type of n,s",type(n),type(s))

            regex="^[A-Z]+"
            mo=re.search(regex,s)
            #push_obj=None

            if mo:
                col=NUM(n,s)
            else:
                col=SYM(n,s)


            if not self.all:
                l = 0
            else:
                l = len(self.all)
            self.all[l]=col
            # COLS.index1= COLS.index1 + 1
            regex1="X$"
            mo1=re.search(regex1,s)
            # col=push_obj
            if not mo1:
                regex2="!$"
                mo2=re.search(regex2,s)
                if mo2:
                    self.klass=col
                regex3="[!+-]$"
                mo3=re.search(regex3,s)
                if mo3:
                    if not self.y:
                        l = 0
                    else:
                        l = len(self.y)
                    self.y[l]=col
                    # COLS.index3 = COLS.index3 + 1

                else:
                    if not self.x:
                        l = 0
                    else:
                        l = len(self.x)
                    self.x[l]=col
                    # COLS.index2 = COLS.index2 + 1


    def add(self,row):
        for t in [self.x,self.y]:
            for _,col in t.items():
                col.add(row.cells[col.at])