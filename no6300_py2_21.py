# -*- coding : utf-8 -*-

#no6300_py2_21.py

# import sys
# sys.stdin = open("ex_075_input.txt", "r")

data = [12, 24, 35, 70, 88, 120, 155]
int_data = list(map(int,data))
new_list = [i for i in int_data if data.index(i)%2!=0]
print(new_list)

