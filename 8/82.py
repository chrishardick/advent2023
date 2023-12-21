#!/usr/local/bin/python3
#==========
# 82.py
#==========

import sys
import re
import math

def lcm(a):
  val = a[0]
  for i in range(1,len(a)):
    val = val*a[i]//math.gcd(val, a[i])
  return val


def all_done (lst):

    for l in lst:
        if l[-1] != 'Z':
            return False

    return True

def update_scratch_list (num_steps, curr_node_list, scratch_list):

    for i in range(len(curr_node_list)):
        if scratch_list[i] == None and curr_node_list[i][-1] == 'Z':
            scratch_list[i] = num_steps

    for i in scratch_list:
        if i == None:
            return False

    return True
        


def print_scratch_list (scratch_list):

    for i in range(len(scratch_list)):
        print (i, " lst=", scratch_list[i])


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


# get starting nodes

starting_nodes = []

for n in node_map:

    if n[-1] == 'A':
        starting_nodes.append(n)
        print ("starting_node=", n)

print ("#starting nodes=", len(starting_nodes))


# list of lists
scratch_list = [None] * len(starting_nodes)



curr_node_list = starting_nodes

num_steps = 0

while True:

    for i in range(len(instr)):

        for n in range(len(curr_node_list)):

            if instr[i] == 'L':
                curr_node_list[n] = node_map[curr_node_list[n]][0]

            elif instr[i] == 'R':
                curr_node_list[n] = node_map[curr_node_list[n]][1]
            
            else:
                print ("Invalid Instruction - ", instr[i])
                sys.exit(-1)

        num_steps = num_steps + 1

        rc = update_scratch_list (num_steps, curr_node_list, scratch_list)

        if rc:
            # have a value for each

            print ("ans=", lcm(scratch_list))

            sys.exit(0)
