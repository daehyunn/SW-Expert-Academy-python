# -*- coding: utf-8 -*_

#no6230_sw35.py

# import sys
# sys.stdin = open("ex_038_input.txt","r",encoding='UTF-8')
#
# N=int(input())
#
# def sosu(a):
#     count = 0
#     for i in range(1,a+1):
#         if a%i==0:
#             count +=1
#     if count ==2:
#         print("소수입니다.")
#     else:
#         print("소수가 아닙니다.")
#
# sosu(N)

# 더욱 단축해보기 -> 런타임 에러가 나왔는데 이유를 모르겠습니다
import sys
import math
sys.stdin = open("ex_038_input.txt","r",encoding='UTF-8')

N=int(input())

def sosu(a):
    count = 0
    for i in range(1, math.ceil(math.sqrt(a)+1)):
        if a%i==0:
            count +=1
    if count ==1:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")

sosu(N)
