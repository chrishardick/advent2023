#!/usr/local/bin/python3
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
mapping_table={
"curr": {
            "next": "xxx",
            "array": [(destination range start, source range start, length), ...], # sorted by source range
        }
 ...
}
'''
mapping_table = {}

# [ (start, len), (start, len), ...]
seeds = []

def get_idx (arr,v):
    
    i = bisect.bisect_left(arr, v, key=lambda x: x[1])  

    if i != len(arr):
        if arr[i][1] == v:    
            pass
        else:
            if i != 0:
                i = i-1
    else:
        if i != 0:
            i = i-1
  
    verbose and print ("get_idx: v: ", v, "idx=", i)
    return i


def print_table_entry (curr):

    print ("curr=")
    print ("{")
    print ("    'next':", curr['next'], ",")
    print ("    'array': [")

    for r in curr['array']:
        print ("    (%s,%s,%s) - src: %s - %s, dest: %s - %s (diff=%s)" % (
            f'{r[0]:20,d}', f'{r[1]:20,d}', f'{r[2]:20,d}',
            f'{r[1]:20,d}', f'{r[1] + r[2]:20,d}',
            f'{r[0]:20,d}', f'{r[0] + r[2]:20,d}',
            f'{r[0] - r[1]:20,d}'
            ))

    print ("    ]")
    print ("}")

def calc_min (minimum, rng_lst):     # [(begin, end), ...]

    for r in rng_lst:
        if minimum == None or r[0] < minimum:
            minimum = r[0]

    return minimum


'''
IN  xxxx  xxx  xxxxxx xxx
       xxxxxxx  xxxxxxx
OUT xxxy  yyy  xYYYYY Yxx   4 ranges
'''
def map_ranges (rng_lst    # [(begin, end), (begin, end), ...]
                ,curr
                ):

    verbose and print ("map_ranges: START: rng_lst=" , rng_lst, " curr=", curr)

    arr = curr["array"]

    out = []

    # [(destination range start, source range start, length), ...]

    verbose and print_table_entry (curr)

    in_range_num = 0

    for r in rng_lst:

        in_range_num = in_range_num + 1

        v = r[0]                # current value of input range
        end = r[0] + r[1]       # end of current input range

        idx = get_idx(arr,v)
  
        verbose and print ("map_ranges: v=", v, "end=", end)

        while v < end and idx < len(arr):       

            min_src_val = arr[idx][1] 
            max_src_val = arr[idx][1] + arr[idx][2]

            diff_val = arr[idx][0] - arr[idx][1]        # dest start - source start

            if v >= min_src_val and v < max_src_val:

                if end > max_src_val:           # input range extends further than this range
                    src_rng_start   = v
                    src_rng_end     = max_src_val

                    idx = idx + 1
                else:                           # input range ends in this range
                    src_rng_start   = v
                    src_rng_end     = end
              
                dest_rng_start = src_rng_start+diff_val
                dest_rng_end   = src_rng_end+diff_val

                length = dest_rng_end-dest_rng_start

                verbose and print ("map_ranges: appending (", dest_rng_start, ", ", length, ")")
                out.append((dest_rng_start, length))

                v = src_rng_end
                
            else:                               # fall-thru

                if v < min_src_val:
                    length = min_src_val - v
                    out.append((v,length))
                    v = min_src_val

                else:
                    idx = idx + 1

        if v < end:
            length = end-v
            verbose and print ("map_ranges: run-off: appending (", v, ", ", length, ")")

            out.append((v,length))

    verbose and print ("map_ranges: out=",out, "\n")

    num_ranges = len(out)

    print ("#ranges: ", num_ranges)

    if num_ranges > 1000:
        print ("LARGE # RANGES. 1ST 1000:")
        for i in range(0,1000):
            print (out[i])
        print ("DONE")

    return out



curr   = ""
dest   = ""

line_num = 0

for line in sys.stdin:

    line_num = line_num + 1

    line = line.rstrip()

    if line_num == 1:       # seeds: 79 14 55 13

        l = line.split(":")
        seeds_lst_str = l[1].split()

        if len(seeds_lst_str) % 2 != 0:
            print ("invalid seeds - %s" % (seeds_lst_str))
            sys.exit (-1)

        # 0, 2, 4, 6
        for i in range(0,len(seeds_lst_str), 2):
            start   = int(seeds_lst_str[i])
            length  = int(seeds_lst_str[i+1])

            seeds.append((start,length))

    elif (match := re.search(r'(.*)-to-(.*) map:',line)):

        curr = match.group(1)
        nxt = match.group(2)

        if curr in mapping_table:

            print ("Error: type already exists in map - ", curr)

            sys.exit(-1)

        mapping_table[curr] = { 
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

        mapping_table[curr]["array"].append((int(ranges[0]), int(ranges[1]), int(ranges[2])))


#
#
#

print ("INPUT - START");
print ("")

print ("seeds = ", seeds)

print ("")

print ("mapping_table=")

for t in mapping_table:

    mapping_table[t]["array"].sort(key=lambda x: x[1])

    print_table_entry (mapping_table[t])
    # print (t, mapping_table[t])

print ("")

print ("INPUT - END")
print ("")
print ("")

#
#
#

minimum = None

for s in seeds:

    print ("MAIN: seed range: ", s)

    curr = 'seed'
    range_list = map_ranges ([s], mapping_table[curr])
   
    nxt = mapping_table["seed"]["next"]     # next label

    while True:

        curr = nxt      # label

        print ("MAIN: curr=", curr)

        range_list = map_ranges (range_list, mapping_table[curr])

        nxt = mapping_table[curr]["next"]

        if nxt == "location":

            minimum = calc_min (minimum, range_list)

            break

print ("minimum=", minimum)
