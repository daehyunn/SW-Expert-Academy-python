# -*- coding: utf-8 -*-
# no 6247_sw29.py

# import sys
# sys.stdin=open("ex_016_input.txt","r")

i=0
j=1
while i<4:
    print(" "*i,end="")
    i += 1
    while j<=4:
        print("*"*(9-2*j)) #2(5-j)-1
        j += 1
        break