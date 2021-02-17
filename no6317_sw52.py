# -*- coding : utf-8 -*-

#no6317_sw52.py

import sys
sys.stdin = open("ex_060_input.txt","r", encoding="UTF-8")

num =3, 5, 4, 1, 8, 10, 2
def maxi(*a):
    return max(a)

print("max{0} => {1}".format(num,maxi(3, 5, 4, 1, 8, 10, 2)))