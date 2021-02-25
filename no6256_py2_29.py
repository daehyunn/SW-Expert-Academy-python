# -*- coding : utf-8 -*-

#no6255_py2_29.py

# import sys
# sys.stdin = open("ex_045_input.txt", "r", encoding="UTF-8")

a = {'아메리카노': 1900,'카페모카':3300,'에스프레소':1900,'카페라떼':2500,'카푸치노':2500,'바닐라라떼':2900}
b = {'헤이즐럿라떼': 2900,'카페모카': 3300, '밀크커피': 3300,'아메리카노': 1900,'샷크린티라떼': 3300}

# 가격 합치기
b.update(a)

# 3000원이상뽑기
high_coffee=set()
item_tuple=tuple()
for key, val in b.items():
    if val>=3000:
        item_tuple=(key,val)
        high_coffee.add(item_tuple)
        item_tuple=()

print(high_coffee)



