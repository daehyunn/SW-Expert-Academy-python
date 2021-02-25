# -*- coding : utf-8 -*-

#no6300_py2_21.py

# import sys
# sys.stdin = open("ex_075_input.txt", "r")

total_list=[]

for i in range(2):
    new_list2=[]
    for j in range(3):
        new_list=[]
        for k in range(4):
            new_list.append(0)
        new_list2.append(new_list)
    new_list=[]
    total_list.append((new_list2))
print(total_list)