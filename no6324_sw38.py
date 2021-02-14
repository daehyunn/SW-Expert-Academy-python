# -*- coding: utf-8 -*_

#no6324_sw38.py

import sys
sys.stdin = open("ex_040_input.txt","r",encoding='UTF-8')

l=[1,2,3,4,3,2,1]

def erase(*a):
    return set(*a)

l2=erase(l)
print(l)
print(list(l2))