#Functions map,kap, sort
#For Lua based functionality
#Not used by test cases unless called explicitly
# List Functions
# map collection

def map_co(t:dict, fun):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(v)
        u[k or (1 + len(u))] = v
    return u


def kap_co(t:dict, fun):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        u[k or 1 + (1 + len(u))] = v
    return u


def sort_co(t:dict, fun):
    dict(sorted(t.items(), fun))
    return t


def keys_co(t):
    return sorted(t.keys())