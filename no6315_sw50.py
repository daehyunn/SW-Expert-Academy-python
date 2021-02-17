# -*- coding : utf-8 -*-

#no6315_sw50.py

import sys
sys.stdin = open("ex_060_input.txt","r", encoding="UTF-8")

num_list = list(range(1,11))
square_list = list(map(lambda x : x*x,num_list))
print(square_list)