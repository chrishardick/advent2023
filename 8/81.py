#!/usr/local/bin/python3
#==========
# 81.py
#==========

import sys
import re


#==========
# main
#==========


# get input, populate instr, node_map

node_map = { }

instr = ""

line_num = 0

for line in sys.stdin:

    line_num = line_num + 1

    line = line.rstrip()

    if line_num == 1:
        instr = line
        continue

    if line == "":
        continue

    l = line.split('=')

    node = l[0].strip()

    s = re.sub (r'[()]','',l[1])

    ss = s.split(',')

    ss[0] = ss[0].strip()
    ss[1] = ss[1].strip()

    node_map[node] = (ss[0], ss[1])


# print data structures

print ("instr=", instr)

print ("node_map")

for n in node_map:

    print ("%s:%s" % (n, node_map[n]))

print ()


num_steps = 0

zzz_found = False

curr_node = 'AAA'

while True:

    for i in range(len(instr)):

        if instr[i] == 'L':
            curr_node = node_map[curr_node][0]

            print ("L curr_node=",curr_node)

        elif instr[i] == 'R':
            curr_node = node_map[curr_node][1]
            
            print ("R curr_node=",curr_node)
        else:
            print ("Invalid Instruction - ", instr[i])
            sys.exit(-1)

        num_steps = num_steps + 1

        if curr_node == "ZZZ":
            zzz_found = True
            break

    if zzz_found:
        break

print ("Num Steps: ", num_steps)

        
    
