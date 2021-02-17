# -*- coding : utf-8 -*-

#no6311_sw46.py

import sys
sys.stdin = open("ex_026_input.txt","r", encoding="UTF-8")

sen = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

#이부분을 람다식으로 변환해야되는데 계속 오류가나와서 해결하지 못함
# def score(x):
#     if x=="A":
#         return int(4)
#     elif x=="B":
#         return int(3)
#     elif x=="C":
#         return int(2)
#     elif x=="D":
#         return int(1)

def change(a):
    sen_list = list(map(ord,a))
    new_list = list(map(lambda x:(69-x),sen_list))
    total = sum(new_list)
    print(total)

change(sen)




