#!/usr/bin/python3
#==========
# 51.py
#==========

import sys
import re
import operator

import bisect

'''
{
"curr": {
            "next": "xxx",
            "array": [(int)], # sorted
            "dict":
               {
                src_range_start(str): [dest range start(int), range length(int)]
               }
        }
 ...
}


"curr": {
            "next": "xxx",
            "array": [(int)], # sorted
            "dict":
               {
                src_range_start(str): [dest range start(int), range length(int)]
               }
        }
 ...
}
'''

types_map = {}

seeds = []


def print_curr (curr):

    print ("curr= { 'next': %s," % (curr["next"]))
    print ("        'array': %s," % (curr["array"]))
    print ("        'dict':")

    for d in sorted(curr["dict"]):

        dd = curr["dict"][d]

        print ("%s: %s" % (d, dd))
        print ("    src[%d-%d]. dest=[%d-%d]" % 
            (d      , d + dd[1], 
            dd[0]   , dd[0] + dd[1] ))
    print ("}")


def get_dest_value (curr
                    ,v
                    ):

    print ("get_dest_value: in: v=", v)
    print_curr(curr)

    arr = curr["array"]
    dct = curr["dict"]

    i = bisect.bisect_left(arr, v)      # index for value less than or equal to v

    if i != len(arr):
        if arr[i] == v:    
            pass
        else:
            if i != 0:
                i = i-1
    else:
        if i != 0:
            i = i-1

    print ("get_dest_value: bisect arr=", arr, " v=", v, " i=", i)

    min_val = arr[i] 
    max_val = arr[i] + dct[arr[i]][1] - 1

    print ("get_dest_value: i=", i, " min=", min_val, " max=", max_val)

    diff = v - min_val

    if v >= min_val and v <= max_val:
        ret = dct[arr[i]][0] + diff

        print ("get_dest_value: ret=", ret, "\n")
        return ret
      
    print ("get_dest_value: no match, ret=", v, "\n")

    return v




curr   = ""
dest   = ""

line_num = 0

for line in sys.stdin:

    line_num = line_num + 1

    line = line.rstrip()

    if line_num == 1:       # seeds: 79 14 55 13

        l = line.split(":")
        seeds = l[1].split()

    elif (match := re.search(r'(.*)-to-(.*) map:',line)):

        curr = match.group(1)
        nxt = match.group(2)

        if curr in types_map:

            print ("Error: type already exists in map - ", curr)

            sys.exit(-1)

        types_map[curr] = { 
                                "next": nxt,
                                "array": [],
                                "dict": {}
                              }

    elif len(line) > 0:

        ranges = line.split()

        if len(ranges) != 3:

            print ("invalid line",line)

            sys.exit(-1)

        # [0] = destination range start
        # [1] = source range start
        # [2] = range length

        types_map[curr]["array"].append(int(ranges[1]))
        types_map[curr]["dict"][int(ranges[1])] = [int(ranges[0]), int(ranges[2])]


for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

print ("seeds", seeds)
print ("")

print ("types_map=")

for t in types_map:

    types_map[t]["array"].sort()

    print (t, types_map[t])

print ("")

seed_to_location = {}

for s in seeds:

    print ("SEED:", s, "\n")

    num = get_dest_value (types_map["seed"], s) # val=num
    
    nxt = types_map["seed"]["next"]     # next label

    while True:

        curr = nxt      # label

        num = get_dest_value (types_map[curr], num)

        nxt = types_map[curr]["next"]

        if nxt == "location":
            
            seed_to_location[s] = num

            break

print (seed_to_location)

min = None

for i in seed_to_location:
    if min == None:
        min = seed_to_location[i]
    elif seed_to_location[i] < min:
        min = seed_to_location[i]

print (min)
