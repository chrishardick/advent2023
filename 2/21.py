#!/usr/bin/python3
#==========
# 21.py
#==========

import sys

sum = 0

for line in sys.stdin:

    max_blue = max_red = max_green = 0

    line = line.rstrip()    # remove any white space from end of string

    print ("line=", line)

    # l[0] = Game X
    # l[1] = subgame list
    l = line.split(":")

    prefix = l[0].split()

    game_id = int(prefix[1])

    print ("game_id=",game_id)

    print ("subgames:", l[1])


    # split by ;
    ll = l[1].split(";")

    # for each subgame
    for sg in ll:

        print ("subgame:", sg)

        colors = sg.split(',')

        print ("colors=%s" % colors)

        blue = red = green = 0

        for c in colors:

            cc = c.split()

            if cc[1] == 'blue':
                blue = int(cc[0])
            elif cc[1] == 'red':
                red = int(cc[0])
            elif cc[1] == 'green':
                green = int(cc[0])
            else:
                print ("ERROR - invalid color", cc[1])

        if blue > max_blue:
            max_blue = blue

        if red > max_red:
            max_red = red

        if green > max_green:
            max_green = green

    if (max_red <= 12 and
        max_green <= 13 and
        max_blue <= 14):

        print ("good!")
        sum = sum + game_id
        
    print ("")

print ("sum=", sum)
