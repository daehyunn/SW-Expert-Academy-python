# -*- coding: utf-8 -*-
# no 6238_sw24.py

import sys
sys.stdin=open("ex_016_input.txt","r")

odd_list=[]
for i in range(1,101,2):
    odd_list.append(i)
print(", ".join(map(str,odd_list)))