# -*- coding:utf-8 -*-

# no6260_py2_33.py

import sys
sys.stdin = open("ex_073_input.txt","r")

data = input()

upper_count = 0
lower_count = 0

for i in data:
    if i.isupper():
        upper_count +=1
    elif i.islower():
        lower_count +=1

print("UPPER CASE {0}".format(upper_count))
print("LOWER CASE {0}".format(lower_count))