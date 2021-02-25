# -*- coding : utf-8 -*-

#no6292_py2_14.py

import sys
sys.stdin = open("ex_065_input.txt", "r")

input_list=list(map(int,input().split(', ')))
print(input_list)
input_tuple = tuple(input_list)
print(input_tuple)