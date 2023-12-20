#!/usr/local/bin/python3
#==========
# 71.py
#==========

import sys
import collections
import functools


def create_default_dict ():

    d = {}

    for c in ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
        d[c] = 0;
       
    return d

card_ranking = {'2': 1, 
                '3': 2, 
                '4': 3,
                '5': 4,
                '6': 5,
                '7': 6,
                '8': 7,
                '9': 8,
                'T': 9,
                'J': 10,
                'Q': 11,
                'K': 12,
                'A': 13}


#==========
# eval_hand
# - hand is a hand dictionary
#
# 5-of-a-kind   7
# 4-of-a-kind   6
# full-house    5
# 3-of-a-kind   4
# 2 pair        3
# 1 pair        2
# high          1
#==========
def eval_hand (hand):

    of_a_kind_5 = 0
    of_a_kind_4 = 0
    of_a_kind_3 = 0
    of_a_kind_2 = 0

    for card in hand:

        if card == 'bid' or card == 'str':
            # not an actual card
            continue

        if hand[card] == 5:

            of_a_kind_5 = of_a_kind_5 + 1

        elif hand[card] == 4:

            of_a_kind_4 = of_a_kind_4 + 1

        elif hand[card] == 3:

            of_a_kind_3 = of_a_kind_3 + 1

        elif hand[card] == 2:

            of_a_kind_2 = of_a_kind_2 + 1


    if of_a_kind_5 > 0:
        return 7

    if of_a_kind_4 > 0:
        return 6

    if of_a_kind_3 > 0 and of_a_kind_2 > 0:
        return 5

    if of_a_kind_3 > 0:
        return 4

    if of_a_kind_2 > 1:
        return 3

    if of_a_kind_2 > 0:
        return 2

    return 1

def eval_hand_str (hand):

    ret = eval_hand(hand)

    if ret == 7:
        return "5-of-a-kind"
    elif ret ==  6:
        return "4-of-a-kind"
    elif ret == 5:
        return "full house"
    elif ret == 4:
        return "3-of-a-kind"
    elif ret == 3:
        return "2 pair"
    elif ret == 2:
        return "a pair"
    elif ret == 1:
        return "single"
    
#==========
# cmp_hands
# - lhs, rhs are hand dictionaries
#==========
def cmp_hands (lhs, rhs):

    l = eval_hand(lhs)
    r = eval_hand(rhs)

    if l < r:
        return -1

    elif l > r:
        return 1

    lhs_str = lhs['str']
    rhs_str = rhs['str']

    for i in range (len(lhs_str)):

        if card_ranking[lhs_str[i]] < card_ranking[rhs_str[i]]:
            return -1
        elif card_ranking[lhs_str[i]] > card_ranking[rhs_str[i]]:
            return 1

    return 0


#==========
# main
#==========
      

hands = []      # ["32T3K"  , "T55J5"   , "KK677"   , "KTJJT"   , "QQQJA"]
bids = []       # [     765 ,   684     ,   28      ,   220     ,   483  ]


# get input

for line in sys.stdin:

    l = line.split()

    hands.append(l[0])
    bids.append(int(l[1]))

print ("hands=",hands)
print ("bids=",bids)



# re-arrange in new list

'''
[
 'A': num,
 'K': num,
 ...
 'str': original string
 'bid': bid
]
'''

l = []

i = 0

for h in hands:

    d = create_default_dict()

    d['bid'] = bids[i]
    d['str'] = h

    hand_str = h

    for idx in range(len(hand_str)):
        d[hand_str[idx]] = d[hand_str[idx]] + 1 

    i = i + 1

    l.append(d)


# sort the new list

l.sort(key=functools.cmp_to_key(cmp_hands))

print ("sorted list:")

for ll in l:
    print (ll, " ", eval_hand_str(ll))

print ("")


# traverse the sorted list and calculate answer

weight = 0

sum = 0

for i in range(len(l)):

    weight = weight + 1

    bid     = l[i]['bid']
    string  = l[i]['str']

    value = weight * bid

    print ("str=", string, " weight=", weight, " bid=", bid, " value=", value, " eval=", eval_hand_str(l[i]))

    sum = sum + value

print ("sum=", sum)
