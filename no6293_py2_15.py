# -*- coding : utf-8 -*-

#no6293_py2_15.py

import sys

sys.stdin = open("ex_066_input.txt", "r")
import math


r_list=list(map(int,input().split(', ')))

def circle_line(a):
    how_long = 2*a*round(math.pi,2)
    return how_long


howlong_list=list(map(circle_line, r_list))

print(", ".join(map(str,howlong_list)))

#출력값이 왜 이렇게 되는건지 소수점 2자리까지 나오게했는데 마지막 요소만 이상한
