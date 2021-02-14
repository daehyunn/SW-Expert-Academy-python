# -*- coding: utf-8 -*_

#no6230_sw35.py

import sys
sys.stdin = open("ex_034_input.txt","r",encoding='UTF-8')

a = input()
b = input()
hand_a = input()
hand_b = input()


def rsp(x,y):
    if x==y:
        print("비겼습니다!")
    elif x=="가위" and y== "바위":
        print("바위가 이겼습니다!")
    elif x=="바위" and y== "가위":
        print("바위가 이겼습니다!")
    elif x=="바위" and y== "보":
        print("보가 이겼습니다!")
    elif x=="보" and y== "바위":
        print("보가 이겼습니다!")
    elif x=="보" and y== "가위":
        print("가위가 이겼습니다!")
    elif x=="가위" and y== "보":
        print("가위가 이겼습니다!")

rsp(hand_a,hand_b)
