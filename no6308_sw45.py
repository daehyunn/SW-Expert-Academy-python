# -*- coding : utf-8 -*-

#no5308_sw45.py

import sys
sys.stdin = open("ex_026_input.txt","r", encoding="UTF-8")

name = input()
age = int(input())

def when_hund(a):
    plus_year = 2019 + (100-a)
    print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(name,plus_year))

when_hund(age)



