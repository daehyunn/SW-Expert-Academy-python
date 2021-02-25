# -*- coding : utf-8 -*-

#no6288_py2_11.py

# import sys
# sys.stdin= open("ex_029_input.txt","r", encoding="UTF-8")


list1 = [i*i for i in range(1,21) if i%3!=0 or i%5!=0]
print(list1)