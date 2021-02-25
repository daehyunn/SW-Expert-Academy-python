# -*- coding:utf-8 -*-

# no6232_py2_37.py

import sys
sys.stdin = open("ex_030_input.txt","r")

data = input()

count =0

for i in range(0,len(data)):
    if data[i] == data[len(data)-1-i]:
        count +=1

if count >= len(data)/2:
    print(data)
    print("입력하신 단어는 회문(Palindrome)입니다.")

