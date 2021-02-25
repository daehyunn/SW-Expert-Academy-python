# -*- coding : utf-8 -*-

#no6254_py2_27.py

import sys
sys.stdin = open("ex_045_input.txt", "r", encoding="UTF-8")

student_phone = {"홍길동":"010-1111-1111", "이순신":"010-1111-2222", "강감찬":"010-1111-3333"}


print("아래 학생들의 전화번호를 조회할 수 있습니다.")
for i in student_phone.keys():
    print(i)

student_name = input("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.\n")
print("{0}의 전화번호는 {1}입니다.".format(student_name,student_phone[student_name]))