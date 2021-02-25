# -*- coding:utf-8 -*-

# no6262_py2_35.py

import sys
sys.stdin = open("ex_096_input.txt","r")

data = input()

how_many = dict()

for i in data:
    how_many[i] = 0
for j in data:
    how_many[j] += 1
for key, val in how_many.items():
    print("{0},{1}".format(key,val))
