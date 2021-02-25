# -*- coding:utf-8 -*-

# no6243_py2_41.py

import sys
sys.stdin = open("ex_097_input.txt","r",encoding="UTF-8")

data = input()

for i in range(0,len(data),2):
    print(data[i], end="")