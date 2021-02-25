# -*- coding:utf-8 -*-

# no6678_py2_40.py

# 몇 행까지 입력할지 모를경우에는 어떻게?
# 그리고 지금 현재 입력값이 결과 값으로 출력이 되어야하는데 그러면 내가 입력을하고 그 값들을 결과값으로 받아오려면?

import sys
sys.stdin = open("ex_070_input.txt","r")

N=3

data = [input().upper() for i in range(N)]

for i in range(N):
    x=input()
    print(data[i])
