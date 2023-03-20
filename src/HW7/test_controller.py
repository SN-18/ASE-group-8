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


def eg(key, string, fun, help):
    egs[key] = fun
    help = help + " -g " + str(key) + "\t" + str(string) + "\n"



#Test for stats
def test_ok(n):
    if n<=0:
        n=1
    n=n or 1
    random.seed(n)


#this is dummy samples, to be deleted,
#just so this doesn't throw errors for now
def samples():
    pass
def test_sample():
    for i in range(1,11):
        emtpy_string=""
        separator=''
        sample_values_tuple=samples(["a","b","c","d","e"]).values()
        print_string=separator.join(sample_values_tuple)
        print(print_string)

def test_num():
    n=NUM()
    for i in range(1,11):
        n.add(i)
    print("",n.n,n.mu,n.sd)

#dummy gaussian func,to be deleted
def gaussian(var1,var2):
    pass
def test_gauss():
    t=[]

    x=1
    y=10**4+1

    for i in range(x,y):
        t.append(gaussian(10,2))

    n=NUM()

    for i in t:
        n.add(i)
    print("",n.n,n.mu,n.sd)

def test_bootmu():
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
def bootstrap():
    pass
#this bootstrap uses an extra argument, check
def test_basic():
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




def test_pre():
    print("\neg3")
    d=1
    for i in range(1,11):
        t1=t2=[]
        for j in range(1,33):
            t1.append(gaussian(10,1))
            t2.append(gaussian(d*10,1))
            print("\t", d, d < 1.1 and True or False, bootstrap(t1, t2), bootstrap(t1, t1))
            d = round(d + 0.05,2)





def test_five():

    pass

def test_six():

    pass

def test_tiles():

    pass

def test_sk():

    pass




