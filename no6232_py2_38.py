# -*- coding:utf-8 -*-

# no6239_py2_38.py


# 문제를 잘못읽어서 단어를 바꾸는건데 철자 전부다 바꿔버림;;
# import sys
# sys.stdin = open("ex_042_input.txt","r")
#
#
# data = list(input())
#
# for i in range(0,int(len(data)/2)):
#     data[i], data[len(data)-1-i] = data[len(data)-1-i], data[i]
#
# print("".join(map(str,data)))


import sys
sys.stdin = open("ex_042_input.txt","r")


data = list(input().split(' '))

for i in range(0,int(len(data)/2)):
    data[i], data[len(data)-1-i] = data[len(data)-1-i], data[i]

print(" ".join(map(str,data)))