# -*- coding : utf-8 -*-

#boj1316.py

import sys
sys.stdin = open("boj1316_testcase2.txt","r")

# 몇 행인지 정보
N = int(input())

# 단어 입력
data = [input() for i in range(N)]
print(data)

is_group_word = 0


for word in data:                                       # data 리스트에서 word를 하나씩 체크
    for index_number in range(len(word)-1):             # 단어의 첫알파벳부터 마지막알파벳-1 까지 체크
        if word[index_number]!=word[index_number+1]:    # 해당 알파벳과 그다음 알파벳이 다른경우
            extra_word = word[index_number+1:len(word)] # 해당 알파벳의 index +1인 알파벳부터 끝까지로 슬라이싱
            if word[index_number] not in extra_word:         # 슬라이싱된 문자열에 해당 알파벳이 없다면                    # 카운트
                is_group_word +=1
                break


print("재사용없는 단어:{0}".format(is_group_word))


