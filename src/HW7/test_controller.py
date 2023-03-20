import numpy as np
import unittest
from functions import *

the, help = {}, '''   
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
'''
from tables import *
from data_loader import *
from globals import the as the
import globals
from data_loader import DATA

egs = {}

class TestEgMethods(unittest.TestCase):

    def test_eg(key, string, fun, help):
        egs[key] = fun
        help = help + " -g " + str(key) + "\t" + str(string) + "\n"



    #Test for stats
    def eg_test_ok(n):
        if n<=0:
            n=1
        n=n or 1
        random.seed(n)


    #this is dummy samples, to be deleted,
    #just so this doesn't throw errors for now
    def eg_samples(self):
        pass

    def eg_test_sample(self):
        for i in range(1,11):
            emtpy_string=""
            separator=''
            sample_values_tuple=samples(["a","b","c","d","e"]).values()
            print_string=separator.join(sample_values_tuple)
            print(print_string)

    def eg_test_num(self):
        n=NUM()
        for i in range(1,11):
            n.add(i)
        print("",n.n,n.mu,n.sd)

    #dummy gaussian func,to be deleted
    def eg_gaussian(var1,var2):
        pass

    def eg_test_gauss(self):
        t=[]

        x=1
        y=10**4+1

        for i in range(x,y):
            t.append(gaussian(10,2))

        n=NUM()

        for i in t:
            n.add(i)
        print("",n.n,n.mu,n.sd)

    def eg_test_bootmu(self):
        a=b=[]
        for i in range(1,101):
            a.append(gaussian(10,1))
        print("","mu","sd","cliffs","boot","both")
        print("","--","--","------","----","----")
        for mu in np.linspace(10,11,11):
            b=[]
            for i in range(1,101):
                b.append(gaussian(mu,1))
            cl=cliffsDelta(a,b)
            bs=bootstrap(a,b, NUM)
            print("",mu,1,cl,bs,cl and bs)

    #dummy bootstrap, to be deleted
    def bootstrap(self):
        pass

    #this bootstrap uses an extra argument, check
    def eg_test_basic(self):
        print("\t\ttruee",bootstrap({8,7,6,2,5,8,7,3}, {8,7,6,5,8,7,3}),
              cliffsDelta({8,7,6,2,5,8,7,3},{8,7,6,2,5,8,7,3}))

        print("\t\tfalse", bootstrap({8, 7, 6, 2, 5, 8, 7, 3},
                                     {9, 9, 7, 8, 10, 9, 6}),
              cliffsDelta({8, 7, 6, 2, 5, 8, 7, 3},
                          {9, 9, 7, 8, 10, 9, 6}))
        print("\t\tfalse",
              bootstrap({0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6},
                        {0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9}),
              cliffsDelta({0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6},
                          {0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9})
              )




    def test_pre(self):
        print("\neg3")
        d=1
        for i in range(1,11):
            t1=t2=[]
            for j in range(1,33):
                t1.append(gaussian(10,1))
                t2.append(gaussian(d*10,1))
                print("\t", d, d < 1.1 and True or False, bootstrap(t1, t2), bootstrap(t1, t1))
                d = round(d + 0.05,2)





    def test_five(self):
        for _,rx in enumerate(tiles(scottKnot(
             [RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"),
             RX({0.6,0.7,0.8,0.9,.6,.7,.8,.9},"rx2"),
             RX({0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35},"rx3"),
             RX({0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9},"rx4"),
             RX({0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4},"rx5")]))):
                print(rx["name"],rx["rank"],rx["show"])


    def test_six(self):
        for i,rx in enumerate(tiles(scottKnot(
                RX({101, 100, 99, 101, 99.5, 101, 100, 99, 101, 99.5}, "rx1"),
                RX({101, 100, 99, 101, 100, 101, 100, 99, 101, 100}, "rx2"),
                RX({101, 100, 99.5, 101, 99, 101, 100, 99.5, 101, 99}, "rx3"),
                RX({101, 100, 99, 101, 100, 101, 100, 99, 101, 100}, "rx4")
        ))):
            print(rx["name"],rx["rank"],rx["show"])




    def test_tiles(self,rxs):
        empty_list=[]
        rxs=a=b=c=d=e=f=g=h=j=k=empty_list
        iter=1

        for iter in range(1,1001): a.append(gaussian(10,1))
        for iter in range(1,1001): b.append(gaussian(10.1,1))
        for iter in range(1, 1001): a.append(gaussian(20, 1))
        for iter in range(1, 1001): a.append(gaussian(30, 1))
        for iter in range(1, 1001): a.append(gaussian(30.1, 1))
        for iter in range(1, 1001): a.append(gaussian(10, 1))
        for iter in range(1, 1001): a.append(gaussian(10, 1))
        for iter in range(1, 1001): a.append(gaussian(40, 1))
        for iter in range(1, 1001): a.append(gaussian(40, 3))
        for iter in range(1, 1001): a.append(gaussian(10, 1))

        for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]): rxs.append(RX(v,"rx" + str(k+1)))

        table.sort(rxs, mid(a) < mid(b))
        for _,rx in enumerate(tiles(rxs)):print("",rx['name'],rx['show'])



    def test_sk(self):
        rxs=a=b=c=d=e=f=g=h=j=k=[]
        for i in range(1,1001):a.append(gaussian(10,1))
        for i in range(1, 1001): b.append(gaussian(10.1, 1))
        for i in range(1, 1001): c.append(gaussian(20, 1))
        for i in range(1, 1001): d.append(gaussian(30, 1))
        for i in range(1, 1001): e.append(gaussian(10, 1))
        for i in range(1, 1001): f.append(gaussian(10, 1))
        for i in range(1, 1001): g.append(gaussian(40, 1))
        for i in range(1, 1001): h.append(gaussian(40, 3))
        for i in range(1, 1001): j.append(gaussian(10, 1))
        for i in range(1, 1001): k.append(gaussian(10, 1))

        for k,v in enumerate(['a','b','c','d','e','f','g','h','j','k']):
            rxs[k]=RX(v,"rx"+str(k+1))
        for _,rx in enumerate(tiles(scottKnot(rxs))):
            print("",rx["rank"],rx["name"],rx["show"])

# for k,fun in enumerate(eg):
#     eg.ok()
#     print("")








