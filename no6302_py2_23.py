# -*- coding : utf-8 -*-

#no6302_py2_23.py

# import sys
# sys.stdin = open("ex_075_input.txt", "r")

data = [12,24,35,70,88,120,155]

new_list =[i for i in data if data.index(i)!=0 and data.index(i)!=4 and data.index(i)!=5]
print(new_list)