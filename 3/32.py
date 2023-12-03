#!/usr/bin/python3
#==========
# 32.py
#==========

import sys
import re

symbols = { '*' }

number_map = { }

def is_numeric (s):

    if re.search ('^[0-9]$', s):
        return True

    return False


#==========
# row_traverse
# - y remains constant
#==========

def row_traverse (rows, y, x):
    
    print ("row_traversal: y=", y, " x=", x)

    min_x = int(x)
    max_x = int(x)
    
    for xx in range(x-1,-1,-1):
        if not is_numeric(rows[y][xx]):
            break
        if xx < min_x:
            min_x = xx

    for xx in range(x+1,len(rows[y])):
        if not is_numeric(rows[y][xx]):
            break
        if xx > max_x:
            max_x = xx

    if (min_x,y) in number_map:
        return 0    # already added


    val = 0

    for i in range (min_x, max_x+1):
        v = int(rows[y][i])

        val = val*10 + v

    number_map[(min_x,y)] = val

    return val

#==========
# symbol_traverse
#==========

def symbol_traverse (rows, y, x):

    if x < 0 or x > len(rows[0])-1:     # invalid x position
        # print ("symbol_traverse: invalid x")
        return

    if y < 0 or y > len(rows)-1:        # invalid y position
        # print ("symbol_traverse: invalid y")
        return

    if not is_numeric(rows[y][x]):      # not numeric   
        # print ("symbol_traverse: not numeric")
        return

    return (row_traverse (rows, y, x))


#==========
# main
#==========

# read input, populate rows

rows = []

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string
    
    rows.append(line)


tot = 0

for y in range(0,len(rows)):
    for x in range (0,len(rows[y])):
        if rows[y][x] in symbols:
            print (rows[y][x], ":", y, ",", x)

            number_map.clear()
            lst = []

            xy_list = [ (y+1,x), (y-1,x), (y,x-1), (y,x+1),     # down, up, left, right
                        (y-1,x-1), (y-1,x+1),                   # top left, top right
                        (y+1,x-1), (y+1,x+1) ]                  # bottom left, bottom right

            for xy in xy_list:
                val = symbol_traverse (rows,xy[0],xy[1])

                if val:
                    if len(lst) < 2:
                        lst.append(val)
                    if len(lst) > 2:
                        break
            
            if len(lst) == 2:
                tot = tot + (lst[0] * lst[1])
                print ("got one: ", lst[0], " ", lst[1]), 

            lst.clear()

print ("sum=", tot)
