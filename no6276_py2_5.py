# -*- coding : utf-8 -*-

#no6276_py2_5.py

# import sys
# sys.stdin= open("ex_026_input.txt","r")


# .더 좋은 방법?


total_list = []

for i in range(2,10):
    gugudan_list = []
    if i%3==0 or i%7==0:
        total_list.append([])
    else:
        for j in range(1,10):
            if j%3!=0 and j%7!=0:
                gugudan_list.append(i*j)
        total_list.append(gugudan_list)
print(total_list)