num_list = list(range(1,201))
new_list = []

for i in range(0, len(num_list)):
    if num_list[i]%7==0 and num_list[i]%5!=0:
        new_list.append(num_list[i])
print(",".join(map(str,new_list)))