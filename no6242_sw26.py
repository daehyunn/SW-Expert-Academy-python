# -*- coding: utf-8 -*-
# no 6242_sw26.py

# import sys
# sys.stdin=open("ex_016_input.txt","r")

bloodtype_list=['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
count_A =0
count_O =0
count_B =0
count_AB =0

for i in bloodtype_list:
    if i == 'A':
        count_A +=1
    elif i == 'O':
        count_O +=1
    elif i == 'B':
        count_B +=1
    else:
        count_AB +=1

total_count={'A':count_A, 'O':count_O, 'B':count_B, 'AB':count_AB}
print(total_count)
