N = int(input())
count = 0
for i in range(1,N+1):
    if N%i == 0:
        print("%d(은)는 %d의 약수입니다." % (i, N))
        count += 1
if count == 2:
    print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (N, 1, N))

# 더 줄이는 방법 고민.. 런타임 에러나서 질문예정
N = int(input())
count = 0
num_set= set()
for i in range(1,int((math.sqrt(N))+1)):
    if N%i == 0:
        count += 1
        num_set.add(i)
        num_set.add(int(N/i))
set_sort=sorted(num_set)

for j in range(0,len(set_sort)):
    print("%d(은)는 %d의 약수입니다." % (set_sort[j], N))

if count == 1:
    print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (N, 1, N))