# -*-coding: utf-8 -*-
# no6251_sw31.py
import sys
sys.stdin = open("ex_020_input.txt", "r")



for i in range(4,-1,-1):
    print(" "*i + "*"*(5-i))
