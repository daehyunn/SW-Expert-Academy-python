# -*- coding: utf-8 -*-
# no 6230_sw21.py

import sys
sys.stdin=open("ex_016_input.txt","r")

score_list=[88,30,61,55,95]
stud_num=1

for i in score_list:
    if i >=60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(stud_num,i))
    else:
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(stud_num, i))
    stud_num += 1