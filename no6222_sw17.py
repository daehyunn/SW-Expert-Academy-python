alpabet = input()

if alpabet.isupper() == 1:
    small_alpa = alpabet.lower()
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(alpabet, ord(alpabet), small_alpa, ord(small_alpa)))
elif alpabet.islower() ==1:
    big_alpa = alpabet.upper()
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(alpabet, ord(alpabet), big_alpa, ord(big_alpa)))
else:
    print(alpabet)