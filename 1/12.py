#!/usr/bin/python3
#==========
# 12.py
#==========

import sys

sum = 0

ss3 = {  'one':    "1"
        ,'two':    "2"
        ,'six':    "6"
        }
   
ss4 = {  'four':    "4"
        ,'five':    "5"
        ,'nine':    "9"
        }

ss5 = {  'three':   "3"
        ,'seven':   "7"
        ,'eight':   "8"
        }


for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    print ("line=",line)

    d1 = None
    s1 = ""

    for i in range (len(line)):

        if line[i].isdigit():
           d1 = line[i]
           break
        else:
            s1 = s1 + line[i]

            print ("s1=", s1, " len=", len(s1))

            if len(s1) >= 5:
                print ("s1 last5=", s1[-5:])
                if s1[-5:] in ss5:
                    d1 = ss5[s1[-5:]]
                    break
                
            if len(s1) >= 4:
                print ("s1 last4=", s1[-4:])
                if s1[-4:] in ss4:
                    d1 = ss4[s1[-4:]]
                    break
                
            if len(s1) >= 3:
                print ("s1 last3=", s1[-3:])
                if s1[-3:] in ss3:
                    d1 = ss3[s1[-3:]]
                    break
                
    d2 = None
    s2 = ""

    print ("")

    for j in range (len(line)-1, -1, -1):
   
        if line[j].isdigit():
            d2 = line[j]
            break
        else:
            s2 = s2 + line[j]

            print ("s2=", s2[::-1], " len=", len(s2))
            
            if len(s2) >= 5:
                print ("s2 last5=", s2[:-6:-1])
                if s2[:-6:-1] in ss5:
                    d2 = ss5[s2[:-6:-1]]
                    break
                
            if len(s2) >= 4:
                print ("s2 last4=", s2[:-5:-1])
                if s2[:-5:-1] in ss4:
                    d2 = ss4[s2[:-5:-1]]
                    break
                
            if len(s2) >= 3:
                print ("s2 last3=", s2[:-4:-1])
                if s2[:-4:-1] in ss3:
                    d2 = ss3[s2[:-4:-1]]
                    break
                
    print ("d1=", d1, "d2=", d2, "\n")

    d = int (d1 + d2)

    sum = sum + d

print (sum)
