# -*- coding : utf-8 -*-

#no6258_py2_31.py

import sys
sys.stdin = open("ex_064_input.txt", "r", encoding="UTF-8")

n=int(input())

dic1=dict()
for key in range(1,n+1):
    dic1[key]=key*key

print(dic1)



