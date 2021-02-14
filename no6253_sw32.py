# -*-coding: utf-8 -*-
# no6253_sw32.py

import sys
sys.stdin = open("EX_input.txt", "r")

num = int(input())
bin_list=[]

while num!=0:
     bin_list.append(num%2)
     num=num//2
     if num==1:
         bin_list.append(num)
         break
for i in range(len(bin_list)-1,-1,-1):
    print(bin_list[i], end="")


