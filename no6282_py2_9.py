# -*- coding : utf-8 -*-

#no6280_py2_7.py

# import sys
# sys.stdin= open("ex_029_input.txt","r", encoding="UTF-8")

n_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
new_list = [x for x in n_list if x%2==0]

print(new_list)

