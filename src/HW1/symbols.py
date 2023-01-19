#contains code for universal objects, SYM and NUM class, which
#are two types of symbols we are using, short for
# symbol and number, respectively

import sys
import math
from table import table as t
import itertools

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

    # def add_child(self, s: str):
    #     self.t[s] = obj.id

# Num class inherited from global object class
# and it's related methods implemented inside of NUM class
class NUM():
    table=t()
    instance_id = next(itertools.count())
    def __init__(self):

        # table = t()
        # super.__init__(s)
        self.id=0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = (-1) * sys.maxsize

    # n_cur is the current n
    def add(self, n_cur: str):
        if n_cur != "?":
            self.n = self.n + 1
            d = n_cur - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n_cur - self.mu)
            self.lo = min(n_cur, self.lo)
            self.hi = max(n_cur, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        var1 = self.m2 < 0 or self.n < 2
        var2 = 0
        var3 = ((self.m2) / (self.n - 1)) ** (0.5)
        return (var1 and var2) or var3



# Symbol class inherited from global object class
# and it's related methods implemented inside of symbol
# sym = SYM("SYM")
class SYM():
    instance_id = next(itertools.count())
    table=t()


    def __new__(cls):

        new_object=object.__new__(cls)
        # object_id=id(new_object)
        # sym_table = t()
        # sym_table.key=object_id
        return new_object

    def __init__(self):
        # super.__init__(s)
        new_object=SYM.__new__(SYM)
        object_id=id(new_object)
        self.id=SYM.instance_id
        SYM.table.value=SYM.instance_id

        # self.address=id(__obj:object)

        # SYM.update()
        # SYM.update_t()


        # self.id=0
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None



    @classmethod
    def update_t(cls,id=0):
        t.key=id

    def obj_table(self):
        print(obj.t)

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



        e_n = 0
        for _, n_cur in self.has.items():
            e_n = e_n + fun(n_cur / self.n)


        return (-1) * e_n