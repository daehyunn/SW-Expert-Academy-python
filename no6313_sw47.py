# -*- coding : utf-8 -*-

#no6311_sw46.py

import sys
sys.stdin = open("ex_060_input.txt","r", encoding="UTF-8")

asc = int(input())

print("ASCII {0} => {1}".format(asc, chr(asc)))