#Stores String Functions, List Functions and Global Functions
#String Functions: 1.) format 2.) oo 3.) o 4.) coerce
#List Functions 1.) map_co 2)kab_co 3.)sort_co 4.)keys , here co is for collections
import math
import table
import re

# Miscalleneous Global Functions
def rand_intpy(lo, hi):
    return math.floor(0.5 + rand_fltpy(lo, hi))


def rand_fltpy(lo, hi, seed):
    lo, hi = lo or 0, hi or 1
    seed = (16807 * seed) % 2147483647
    return seed, lo + (hi - lo) * seed / 2147483647


def round_n(n, nPlaces=3):
    multiplier = 10 ** (nPlaces)
    return math.floor(n*multiplier+ 0.5)/multiplier





def coerce(s):
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