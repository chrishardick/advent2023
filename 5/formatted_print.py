#!/usr/local/bin/python3
#==========
# formatted_print.py
#==========

num=1_000_000_000_000

print ("|",f'{num:20,d}',"|")

print ("|%s|" % (f'{num:20,d}'))
