# -*- coding: utf-8 -*_

#no6326_sw40.py

import sys
sys.stdin = open("ex_063_input.txt","r",encoding='UTF-8')

N=int(input())

def fac(a):
    fac_num=1
    for i in range(1, a+1):
        fac_num = fac_num *i
    return fac_num

print(fac(N))

