#!/usr/local/bin/python3
#==========
# 52.py
#==========



import sys
import re
import operator

import bisect

verbose = False

def get_idx (arr,v):
    
    i = bisect.bisect_left(arr, v, key=lambda x: x[1])  

    print ("len=", len(arr))
    print ("i=", i)

    if i != len(arr):
        if arr[i][1] == v:    
            pass
        else:
            if i != 0:
                i = i-1
    else:
        if i != 0:
            i = i-1
  
    print ("get_idx: v: ", v, "idx=", i)
    return i

arr = [
(81,45,19)
,(68, 64, 13)
,(45, 77, 23)
]

print ("arr=",arr)

print ("idx(77)", get_idx(arr,77))
