# -*- coding : utf-8 -*-

#no6303_py2_24.py

# import sys
# sys.stdin = open("ex_075_input.txt", "r")

data = [12,24,35,24,88,120,155,88,120,155]

def clear_list(*a):
    set_data = set(data)
    clear_data = list(set_data)
    clear_data.sort()
    return clear_data

print(clear_list(data))