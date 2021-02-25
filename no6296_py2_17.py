# -*- coding : utf-8 -*-

#no6296_py2_17.py

import sys
sys.stdin = open("ex_068_input.txt", "r")

# 인풋의 변할때는 변수의 갯수를 어떻게 지정하는지

word1, word2, word3, word4 = input().split(', ')

word_list = [word1, word2, word3, word4]
word_list.sort()
print(", ".join(word_list))