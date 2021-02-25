# -*- coding : utf-8 -*-

#no6280_py2_11.py

# import sys
# sys.stdin= open("ex_029_input.txt","r", encoding="UTF-8")


n = 10

def fibo(a):
    if a <=1:
        return 1
    else:
        return fibo(a-1) + fibo(a-2)

fibo_list = [fibo(i) for i in range(n)]
print(fibo_list)


