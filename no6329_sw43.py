# -*- coding: utf-8 -*_

#no6326_sw40.py

import sys
sys.stdin = open("ex_078_input.txt","r",encoding='UTF-8')

def countdown(a):
    if a <=0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for i in range(a,0,-1):
            print(i)

countdown(0)
countdown(10)

