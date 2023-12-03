#!/usr/bin/python3
#==========
# getchars.py
#==========

import sys

char_dict = {}

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string
    
    for c in line:
        if c not in char_dict:
            char_dict[c] = 1;
        else:
            char_dict[c] = char_dict[c] + 1

for c in char_dict:
    print (c, " => ", char_dict[c])

