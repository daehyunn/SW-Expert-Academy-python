# -*- coding : utf-8 -*-

#no6273_py2_3.py

# import sys
# sys.stdin= open("ex_026_input.txt","r")


stud1 = (90, 80)
stud2 = (85, 75)
stud3 = (90, 100)

score_list = [stud1,stud2, stud3]

for i in score_list:
    total = sum(i)
    aver = sum(i)/2
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2}입니다.".format(score_list.index(i)+1, total, aver))