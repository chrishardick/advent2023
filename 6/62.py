#!/usr/local/bin/python3
#==========
# 62.py
#==========

'''
Time:      7  15   30
Distance:  9  40  200
'''

import sys

time = 0
distance = 0

# read input

for line in sys.stdin:

    l = line.split(":")
   
    if len(l) != 2:
        print ("Invalid Line")
        sys.exit(-1)

    fld = l[1].split()

    if l[0] == 'Time':

        time_str = ''

        for f in fld:
            time_str = time_str + f

        time = int(time_str)

    elif l[0] == 'Distance':

        distance_str = ''

        for f in fld:
            distance_str = distance_str + f

        distance = int(distance_str)


# print input

print ("Time: ", time)
print ("Distance: ", distance)

num_ways = 0

for hold_tm in range (1,time):
        
    speed = hold_tm

    tot = speed * (time - hold_tm)

    if tot > distance:
        num_ways = num_ways + 1

print ("num_ways=", num_ways)
