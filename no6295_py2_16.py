# -*- coding : utf-8 -*-

#no6295_py2_16.py

import sys
sys.stdin = open("ex_067_input.txt", "r")

row, col = map(int,input().split(', '))

total_list=[]
new_list = []

for i in range(0,row):
    for j in range(0,col):
        new_list.append(i*j)
    total_list.append(new_list)
    new_list=[]

print(total_list)