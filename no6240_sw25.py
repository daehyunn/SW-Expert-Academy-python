# -*- coding: utf-8 -*-
# no 6240_sw25.py

# import sys
# sys.stdin=open("ex_016_input.txt","r")

total=0

for i in range(1,101):
    if i%3==0:
        total += i
print("1부터 100사이의 숫자 중 3의 배수의 총합: {0}".format(total))