# -*- coding: utf-8 -*_
#
# no6319_sw34.py


import sys
sys.stdin = open("ex_031_input.txt", "r")
#
# word = "qwer"
# print(word[0])
#
# def reverse(a):
#     for i in range(0,len(word)//2):
#         word[i],word[len(word)-1-i] = word[len(word)-1-i], word[i]
#     return a
#
# reverse_word = reverse(word)
# print("{0}".format(reverse_word))
#
# if word == reverse(word):
#     print("입력하신 단어는 회문(Palindrome)입니다.")

word = input()

def reverse(a):
    word_list=list(a)
    rev_word=""
    for j in range(len(word_list)):
        rev_word+=word_list.pop()
    return rev_word

reverse_word = reverse(word)
print("{0}".format(reverse_word))

if word == reverse(word):
    print("입력하신 단어는 회문(Palindrome)입니다.")