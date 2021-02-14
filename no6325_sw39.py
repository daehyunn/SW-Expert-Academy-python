# -*- coding: utf-8 -*_

#no6324_sw38.py

import sys
sys.stdin = open("ex_040_input.txt","r",encoding='UTF-8')

l=[2,4,6,8,10]

def find(n):
    if n in l:
        print("{0} => True".format(n))
    else:
        print("{0} => False".format(n))

print(l)
find(5)
find(10)
