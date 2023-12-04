#!/usr/bin/python3
#==========
# 41.py
#==========

import sys

tot = 0

# for each card

for line in sys.stdin:

    line = line.rstrip()

    # l[0] = "Card 1"
    # l[1] = "41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    l = line.split(":")

    card_num = (l[0].split())[1]

    # wl[0] = "41 48 83 86 17"
    # wl[1] = "83 86  6 31 17  9 48 53"
    wl = l[1].split("|")

    winning_numbers_strings = wl[0].split()
    our_numbers_strings     = wl[1].split()

    winning_numbers = set()

    for w in winning_numbers_strings:
        winning_numbers.add(int(w))

    num_winners = 0

    for o in our_numbers_strings:
        if int(o) in winning_numbers:
            num_winners = num_winners + 1

    print ("card#",card_num, " #win=",num_winners)

    if (num_winners > 0):
        num = 2**(num_winners-1)
        tot = tot + num


print (tot)



    
