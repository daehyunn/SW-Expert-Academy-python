# -*- coding : utf-8 -*-

#no6276_py2_5.py

# 리스트 내포기능 활용?
import sys
sys.stdin= open("ex_024_input.txt","r", encoding="UTF-8")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

score_list = [a,b,c,d,e]
avg = sum(score_list)/len(score_list)

print("입력된 값 {0}의 평균은 {1}입니다.".format(score_list, avg))