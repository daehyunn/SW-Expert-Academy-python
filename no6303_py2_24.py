# -*- coding : utf-8 -*-

#no6303_py2_24.py

# import sys
# sys.stdin = open("ex_075_input.txt", "r")


data1 = [1,3,6,78,35,55]
data2 = [12,24,35,24,88,120,155]

same_list = [i for i in data1 if i in data2]
print(same_list)