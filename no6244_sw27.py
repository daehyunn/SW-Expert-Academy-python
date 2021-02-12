# -*- coding: utf-8 -*-
# no 6244_sw27.py

# import sys
# sys.stdin=open("ex_016_input.txt","r")

score_list=[85,65,77,83,75,22,98,88,38,100]
over_list=[]
total_score=0

for i in score_list:
    while i>=80:
        over_list.append(i)
        total_score += over_list.pop()
        break
print(total_score)
