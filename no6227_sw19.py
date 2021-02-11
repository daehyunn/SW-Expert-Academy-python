num_list = list(range(100,301))
new_list = []

for i in range(0, len(num_list)):
    hund_num = num_list[i] // 100 #백의자리 추출
    ten_num = (num_list[i] - 100 * hund_num) // 10 #십의자리 추출
    one_num = (num_list[i] - 100 * hund_num - 10 * ten_num) // 1 #일의자리 추출
    if hund_num%2==0 and ten_num%2==0 and one_num%2==0:
        new_list.append(num_list[i])
print(",".join(map(str, new_list)))