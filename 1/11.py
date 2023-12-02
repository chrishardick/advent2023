#!/usr/bin/python3
#==========
# 11.py
#==========

import sys

sum = 0

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    d1 = None
    d2 = None

    for i in range (len(line)):

        if line[i].isdigit():
           d1 = line[i]
           break

    for j in range (len(line)-1, -1, -1):
   
        if line[j].isdigit():
            d2 = line[j]
            break;

    d = int (d1 + d2)

    sum = sum + d

print (sum)
