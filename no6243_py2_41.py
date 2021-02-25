# -*- coding:utf-8 -*-

# no6243_py2_41.py

import sys
sys.stdin = open("ex_070_input.txt","r",encoding="UTF-8")

data = input().split(' ')

data_set=set(data)
print(",".join(map(str,sorted(data_set))))