# -*- coding : utf-8 -*-

#no6275_py2_4.py

# import sys
# sys.stdin= open("ex_026_input.txt","r")

# 좀더 좋은 방법?
sent = list('Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.')

delete_list = [i for i in sent if i!="a" and i!="e" and i!="i" and i!="o" and i!="u"]

print("".join(delete_list))