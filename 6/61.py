#!/usr/local/bin/python3
#==========
# 61.py
#==========

'''
Time:      7  15   30
Distance:  9  40  200
'''

import sys

time = []
distance = []

# read input

for line in sys.stdin:

    l = line.split(":")
   
    if len(l) != 2:
        print ("Invalid Line")
        sys.exit(-1)

    fld = l[1].split()

    if l[0] == 'Time':

        for f in fld:
            time.append(int(f))

    elif l[0] == 'Distance':

        for f in fld:
            distance.append(int(f))


# print input

print ("Time: ", time)
print ("Distance: ", distance)


num_races = len(time)

results = []

for race_num in range (num_races):

    tm = time[race_num]

    num_ways = 0

    for hold_tm in range (1,tm):
        
        speed = hold_tm

        tot = speed * (tm - hold_tm)

        if tot > distance[race_num]:
            num_ways = num_ways + 1

    results.append(num_ways)


product = 1

for r in results:

    product = product * r

print ("product=", product)
