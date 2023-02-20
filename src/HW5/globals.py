the, help = {},\
'''   
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -b  --bins   initial number of bins      = 16
  -c  --cliffs cliff's delta threshold     = 0.147
  -f  --file   name of file                = ./auto93.csv
  -F  --Far    distance on distant         = 0.95
  -g  --go     start-up action             = data
  -h  --help   show help                   = false
  -H  --Halves search space for clustering = 512
  -m  --min    size of smallest cluster    = 0.5
  -M  --Max    numbers                     = 512
  -p  --p      distance coefficient        = 2
  -r  --rest   how many of rest to sample  = 4
  -R  --Reuse  child splits reuse a parent pole = true
  -s  --seed   random number seed          = 937162211
ACTIONS:
'''
seed = 937162211
b4 = {}
magic = "\n[%s]+[-][%S][%s]+[-][-]([%S]+)[^\n]+= ([%S]+)"