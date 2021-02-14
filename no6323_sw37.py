# -*- coding: utf-8 -*_

#no6323_sw37.py

import sys
sys.stdin = open("ex_040_input.txt","r",encoding='UTF-8')

#횟수
## 너무 안풀려서 검색해봄...

N=int(input())

def fibo(n):
    return fibo(n-1) + fibo(n-2) if n>=2 else n # 이부분도 리턴부분에 조건식을 더 붙일수 있는건지

fibo_list=[]

for i in range(1,N+1):
    fibo_list.append(fibo(i))
print(fibo_list)


