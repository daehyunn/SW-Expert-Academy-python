# -*- coding:utf-8 -*-

# no6239_py2_38.py

import sys
import re
sys.stdin = open("ex_050_input.txt","r")

data = input().split('/')

print("protocol: {0}".format(data[0]))
print("host: {0}".format(data[2]))
print("others: {0}".format(data[3]))


# 입력 데이터를 분리하는 방법??