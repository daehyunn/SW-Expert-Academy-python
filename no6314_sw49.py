# -*- coding : utf-8 -*-

#no6314_sw49.py

import sys
sys.stdin = open("ex_060_input.txt","r", encoding="UTF-8")

num_list = list(range(1,11))
even_list = list(filter(lambda x : x%2==0,num_list))
print(even_list)