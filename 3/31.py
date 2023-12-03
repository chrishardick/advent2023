#!/usr/bin/python3
#==========
# 31.py
#==========

import sys
import re

symbols = { '*', '#', '+', '$', '/', '=', '%', '@', '&', '-' }

number_map = { }

def is_numeric (s):

    if re.search ('^[0-9]$', s):
        # print ("numeric: ",s)
        return True

    # print ("NOT numeric: ",s)
    return False


#==========
# col_traverse
# - x remains constant
#==========

def col_traverse (rows, y, x):

    print ("col_traversal: y=", y, " x=", x)

    min_y = int(y)
    max_y = int(y)
    
    for yy in range(y-1,-1,-1):
        if not is_numeric(rows[yy][x]):
            break
        if yy < min_y:
            min_y = yy

    for yy in range(y+1,len(rows)):
        if not is_numeric(rows[yy][x]):
            break
        if yy > max_y:
            max_y = yy

    if (x,min_y) in number_map:
        return      # already added


    print ("col_traversal: min_y=", min_y, " max_y=", max_y)

    val = 0

    for i in range (min_y, max_y+1):
        # print ("col_traversal: i=", i)
        v = int(rows[i][x])

        val = val*10 + v

    number_map[(x,min_y)] = val
        

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
        return      # already added


    val = 0

    for i in range (min_x, max_x+1):
        v = int(rows[y][i])

        val = val*10 + v

    number_map[(min_x,y)] = val


#==========
# symbol_traverse
#==========

def symbol_traverse (rows, y, x):

    # print ("symbol_traverse: y=", y, " x=", x)

    if x < 0 or x > len(rows[0])-1:     # invalid x position
        # print ("symbol_traverse: invalid x")
        return

    if y < 0 or y > len(rows)-1:        # invalid y position
        # print ("symbol_traverse: invalid y")
        return

    if not is_numeric(rows[y][x]):      # not numeric   
        # print ("symbol_traverse: not numeric")
        return

    #col_traverse (rows, y, x)
    row_traverse (rows, y, x)


#==========
# main
#==========

# read input, populate rows

rows = []

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string
    
    rows.append(line)


for y in range(0,len(rows)):
    for x in range (0,len(rows[y])):
        if rows[y][x] in symbols:
            print (rows[y][x], ":", y, ",", x)
            symbol_traverse (rows,y-1, x)        # up
            symbol_traverse (rows,y+1, x)        # down
            symbol_traverse (rows,y, x-1)        # left
            symbol_traverse (rows,y, x+1)        # right
            symbol_traverse (rows,y-1,x-1)       # top left
            symbol_traverse (rows,y-1,x+1)       # top right
            symbol_traverse (rows,y+1,x-1)       # bottom left
            symbol_traverse (rows,y+1,x+1)       # bottom right
     
sum = 0

for i in number_map:
    print (number_map[i])
    sum = sum + number_map[i]

print ("sum=", sum)
