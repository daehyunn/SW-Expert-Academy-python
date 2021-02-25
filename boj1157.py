# -*- coding:utf-8 -*-

# boj1157.py

import sys
sys.stdin = open("boj1157_testcase1.txt","r")

# 인풋을 전부 대문자화
data = input().upper()

#알파벳을 카운트하기위한 딕셔너리 만들기
alpa_dic = {}
for i in range(65,91):
    alpa_dic[chr(i)]=0

# 인풋데이터의 알파벳을 key로 가지는 것의 갯수를 추가
for j in data:
    alpa_dic[j]+=1

# value 값을 가지고 key를 찾는 함수를 정의하는데 이떄 찾고자하는 key가 2개인 경우 고려
def find_key(a):
    count = 0
    for key, val in alpa_dic.items():
        if val == a:
            count += 1
            one_key = key
    if count==1:
        print("{0}".format(one_key))
    else:
        print("?")

find_key(max(alpa_dic.values()))

