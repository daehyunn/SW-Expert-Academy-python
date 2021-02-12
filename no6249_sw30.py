# -*- coding: utf-8 -*-
# no 6249_sw30.py

# import sys
# sys.stdin=open("ex_018_input.txt","r")
#
# N=int(input())
# N_split=[]
#
# while N!=0:
#     N_split.append(N%10)
#     N=N//10
# print(N_split[0])
#
# count_0 = N_split.count(0)
# count_1 = N_split.count(1)
# count_2 = N_split.count(2)
# count_3 = N_split.count(3)
# count_4 = N_split.count(4)
# count_5 = N_split.count(5)
# count_6 = N_split.count(6)
# count_7 = N_split.count(7)
# count_8 = N_split.count(8)
# count_9 = N_split.count(9)
#
# print("0 1 2 3 4 5 6 7 8 9")
# print("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9))


# 위에는 기존에 햇던 코드 밑에는 좀 더 단축을 위해서
import sys
sys.stdin=open("ex_018_input.txt","r")

N=int(input())
N_split=[0 for i in range(10)]

while N != 0:
    N_split[N%10] += 1
    N=N//10
print("0 1 2 3 4 5 6 7 8 9")
for j in range(10):
    print(N_split[j], end=" ") # 여기서 join(map 이런거도 잘 써지고  sep= 이걸르 쓰고싶은데 앞에 형식에 따라 다른것같아서 질문

