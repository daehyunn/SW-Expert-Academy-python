# -*- coding : utf-8 -*-

#no6299_py2_20.py

# import sys
# sys.stdin = open("ex_075_input.txt", "r")

data = [12, 24, 35, 70, 88, 120, 155]
int_data = list(map(int,data))
new_list = [i for i in int_data if i%2!=0]
print(new_list)
print(type(data))

