# -*- coding : utf-8 -*-

#no6255_py2_28.py

# import sys
# sys.stdin = open("ex_045_input.txt", "r", encoding="UTF-8")

data = {"TV":2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}

data_values = sorted(data.values(), reverse=1)

def find_key(val):
    for key, value in data.items():
        if val==value:
            return key

for i in data_values:
    print("{0}: {1}".format(find_key(i), i))