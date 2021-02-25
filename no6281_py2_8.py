# -*- coding : utf-8 -*-

#no6280_py2_7.py

import sys
sys.stdin= open("ex_029_input.txt","r", encoding="UTF-8")

n = int(input())

num_list = [x for x in range(1,n+1) if n%x==0]
print(num_list)