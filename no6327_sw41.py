# -*- coding: utf-8 -*_

#no6326_sw40.py

import sys
sys.stdin = open("ex_077_input.txt","r",encoding='UTF-8')

N1, N2 = map(int, input().split(", "))

def square(a):
    a= a ** 2
    return a

print("square({0}) => {1}".format(N1, square(N1)))
print("square({0}) => {1}".format(N2, square(N2)))



