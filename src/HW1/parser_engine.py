#contains code for cli interaction, to set user settings (as user inputs them)
#

import sys
# import re
from functions import *

'''
the, help = {},[[   
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
]]
'''

def cli(options):
    args = sys.argv[1:]
    for k, v in options.items():
        v = str(v)
        for n, x in enumerate(args):
            if x == '-' + k[0] or x == '--' + k:
                if v == 'false':
                    v = 'true'
                elif v == 'true':
                    v = 'false'
                else:
                    v = args[n + 1]
            options[k] = coerce(v)
    return options




def settings(s:str):
    regex="\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
    mo=re.findall(regex,s)
    d=dict(mo)
    return d




# scontrol="%s %s"
# actual string->unpack

# print("%s %s","a","b")
# sControl_modified="{" + sControl + "}"
# print("{sControl}"$).format
# print()


# NUM,SYM = obj("NUM"), obj("SYM")




