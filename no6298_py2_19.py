# -*- coding : utf-8 -*-

#no6297_py2_18.py

# import sys
# sys.stdin = open("ex_075_input.txt", "r")

data = (1,2,3,4,5,6,7,8,9,10)
list1 = []
list2 = []

for i in range(0,int(len(data)/2)):
    list1.append(data[i])
for j in range(int(len(data)/2),len(data)):
    list2.append((data[j]))

tuple1=tuple(list1)
tuple2=tuple(list2)

print(tuple1)
print(tuple2)
