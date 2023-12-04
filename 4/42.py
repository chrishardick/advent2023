#!/usr/bin/python3
#==========
# 42.py
#==========

import sys

# card# -> #winners
card_data = {}

# [card#, card#, card#, ...]
winning_card_list = []

# for each card

num = 0

for line in sys.stdin:

    num = num + 1

    line = line.rstrip()

    # l[0] = "Card 1"
    # l[1] = "41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    l = line.split(":")

    card_num = int((l[0].split())[1])

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

    card_data[card_num] = num_winners

    for i in range(card_num+1, card_num + num_winners + 1):
        winning_card_list.append(i)


for card_num in winning_card_list:
    num = num + 1

    num_winners = card_data[card_num]

    for i in range(card_num+1, card_num + num_winners + 1):
        winning_card_list.append(i)

print (num)
