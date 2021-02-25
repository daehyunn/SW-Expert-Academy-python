# -*- coding : utf-8 -*-

#no6258_py2_31.py

import sys
sys.stdin = open("ex_072_input.txt", "r", encoding="UTF-8")

data = input()

word_count=0
num_count=0
dic = dict()


for i in data:
    if ord(i)>=65 and ord(i)<=122:
        word_count +=1
    elif ord(i)>=48 and ord(i)<=57:
        num_count +=1
dic["LETTERS"]=word_count
dic["DIGITS"]=num_count

for key, val in dic.items():
    print("{0} {1}".format(key,val))


