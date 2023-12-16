#!/usr/bin/python3
#==========
# 52.py
#==========


''' 
seeds are now pairs [start, range]
- there are now a HUGE NUMBER of seeds

for each seed
    seed to soil
    soil to fertilizer
    fertilizer to water
    water to light
    light to temperature
    temperature to humidity
    humidity to location
'''

import sys
import re
import operator

import bisect

verbose = False

'''
types_map={
"curr": {
            "next": "xxx",
            "array": [(destination range start, source range start, length), ...], # sorted by source range
        }
 ...
}
'''
types_map = {}

seeds = []

def get_idx (arr,v):
    
    i = bisect.bisect_left(arr, v, key=lambda x: x[1])  

    if i != len(arr):
        if arr[i] == v:    
            pass
        else:
            if i != 0:
                i = i-1
    else:
        if i != 0:
            i = i-1
   
    return i

'''
IN  xxxxxxxxxxxxxxxxx
       xxxxxxx  xxxxxxx
OUT xxxyyyyyyyxxYYYYY       4 ranges
'''
def map_ranges (curr
                ,rng    # [begin, end)
                ):

    arr = curr["array"]

    out = []

    # [(destination range start, source range start, length), ...]

    v = rng[0]
    end = rng[0] + rng[1]

    idx = get_idx(arr,v)

    while v < end and idx < len(arr):

        min_src_val = arr[idx][1] 
        max_src_val = arr[idx][1] + arr[idx][2] - 1

        diff_valdiff = arr[idx][1] - arr[idx][0]        # src_start - dest_start 

        if v >= min_src_val and v <= max_src_val:

            if end > max_src_val:
                src_rng_start   = v
                src_rng_end     = max_src_val

                idx = idx + 1
            else:
                src_rng_start   = v
                src_rng_end     = end
                
            out.append(src_rng_start-diff_val, src_rng_end-diff_val+1)

            v = src_rng_end+1
                
        else:
            out.append(v,v+1)
            v = v+1

    return out



curr   = ""
dest   = ""

line_num = 0

for line in sys.stdin:

    line_num = line_num + 1

    line = line.rstrip()

    if line_num == 1:       # seeds: 79 14 55 13

        l = line.split(":")
        seeds_pre = l[1].split()

        if len(seeds_pre) % 2 != 0:
            print ("invalid seeds - %s" % (seeds_pre))
            sys.exit (-1)

        # print ("seeds_pre: %s" % (seeds_pre))

        # 1, 3
        for i in range(0,len(seeds_pre), 2):
            start = int(seeds_pre[i])
            num = int(seeds_pre[i+1])

            seeds.append((start,num))

    elif (match := re.search(r'(.*)-to-(.*) map:',line)):

        curr = match.group(1)
        nxt = match.group(2)

        if curr in types_map:

            print ("Error: type already exists in map - ", curr)

            sys.exit(-1)

        types_map[curr] = { 
                                "next": nxt,
                                "array": [],
                              }

    elif len(line) > 0:

        ranges = line.split()

        if len(ranges) != 3:

            print ("invalid line",line)

            sys.exit(-1)

        # [0] = destination range start
        # [1] = source range start
        # [2] = range length

        types_map[curr]["array"].append((int(ranges[0]), int(ranges[1]), int(ranges[2])))

print ("seeds = ", seeds)

print ("types_map=")

for t in types_map:

    types_map[t]["array"].sort(key=lambda x: x[1])

    print (t, types_map[t])

print ("")

sys.exit(0)


curr_min_seed   = None
curr_min_val    = None

num_seed = 0

for i in seed_map:

    start = i
    end = i+seed_map[i]

    range_list = map_ranges (types_map["seed"], (start, end)) # val=num
    
    nxt = types_map["seed"]["next"]     # next label

        while True:

            curr = nxt      # label

            range_list = map_range (get_dest_value (range_list, (start, end))

            nxt = types_map[curr]["next"]

            if nxt == "location":
            
                if curr_min_val == None or num < curr_min_val:
                    curr_min_val = num
                    curr_min_seed = s

                    print ("new min: ", curr_min_val, " seed=", curr_min_seed)

                break

print ("min=",curr_min_val, "seed=", curr_min_seed)
