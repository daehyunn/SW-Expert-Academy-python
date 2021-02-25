# -*- coding : utf-8 -*-

#no6297_py2_18.py

import sys
sys.stdin = open("ex_075_input.txt", "r")

data = list(map(int,input().split(', ')))

odd_list = list(filter(lambda x: x%2!=0, data))
print(", ".join(map(str,odd_list)))