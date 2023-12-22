#!/usr/local/bin/python3
#==========
# 91.py
#==========

import sys
import re


dbg = True


def get_next (arr):

    print ("get_next: IN: ", arr)

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

        print ("get_next: lcl=", lcl_arr)

        if not all_zero:
            matrix.append(lcl_arr)

        else:
            break


    for i in range (len(matrix)-1,-1,-1):
        if i == len(matrix)-1:
            append_val = matrix[i][-1]
        else:
            append_val = append_val + matrix[i][-1]

        matrix[i].append(append_val)

    return append_val



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

    val = get_next(line)

    print ("next=", val)
    print ("")

    sum = sum + val


print ("")

print ("sum=",sum)





