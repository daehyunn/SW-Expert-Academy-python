# -*- coding: utf-8 -*_

#no6326_sw40.py

import sys
sys.stdin = open("ex_078_input.txt","r",encoding='UTF-8')

word1, word2= map(str,input().split())
def longer(a,b):
    if len(a)>len(b):
        print(a)
    else:
        print(b)

longer(word1,word2)
