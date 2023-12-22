#!/usr/local/bin/python3
#==========
# 92.py
#==========

import sys
import re


dbg = True


def get_prev (arr):

    print ("get_prev: IN: ", arr)

    matrix = []

    matrix.append(arr)

    while True:
        
        lcl_arr = []

        all_zero = True

        a = matrix[-1]

        for i in range (len(a)-1):

            diff = a[i+1] - a[i]

            if diff != 0:
                all_zero = False

            lcl_arr.append(diff)

        print ("get_prev: lcl=", lcl_arr)

        if not all_zero:
            matrix.append(lcl_arr)

        else:
            break


    pre_values = [0] * len(matrix)

    # start at bottom of matrix and work upwards

    for y in range (len(matrix)-1,-1,-1):
        if y == len(matrix)-1:
            # bottom row
            pre_val = matrix[y][0]
        else:
            # not the bottom row
            pre_val = - (pre_values[y+1] - matrix[y][0])

        pre_values[y] = pre_val

    return pre_val



#==========
# main
#==========

# parse input, load matrix

matrix = []

for line in sys.stdin:

    line = line.rstrip()

    l = line.split()

    nums = []

    for i in range(len(l)):
        nums.append(int(l[i]))

    matrix.append(nums);


# print matrix

print ("matrix")

sum = 0

for line in matrix:

    print (line)

    val = get_prev(line)

    print ("next=", val)
    print ("")

    sum = sum + val


print ("")

print ("sum=",sum)





