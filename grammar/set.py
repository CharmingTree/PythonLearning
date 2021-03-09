## 멱집합 생성
#a = [1,2,3,4]
a = ['a','b','c']
powerSet = []

a_size = len(a)
for i in range(2**a_size):
    flag = bin(i)[2:].zfill(a_size)
    print(flag)
    subset = [a[j] for j in range(a_size) if flag[j] == '1']
    powerSet.append(subset)

print(powerSet)
