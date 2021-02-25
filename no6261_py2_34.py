# -*- coding:utf-8 -*-

# no6260_py2_33.py

# import sys
# sys.stdin = open("ex_073_input.txt","r")

beer_price = {'하이트': 2000, '카스': 2100, '칭따오':2500, '하이네켄':4000,'버드와이저':500}
print(beer_price)


for key,val in beer_price.items():
    beer_price[key] = val*(1.05)

print(beer_price)


