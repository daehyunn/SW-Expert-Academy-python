# -*- coding : utf-8 -*-

#no6289_py2_12.py

import sys
sys.stdin= open("ex_051_input.txt","r", encoding="UTF-8")

num = input()
num_list = list(num)
int_list = list(map(int,num_list))

print("{0}".format(sum(int_list)))