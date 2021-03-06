

# B에 A를 얕은 복사 
a = [1,2,3,4]
b = a[:]

# 얕은 복사이기 떄문에 id가 다르다
print(id(a))
print(id(b))

# 리스트 요소 역시 A, B 서로 다르다
b.append(5)

print(a)
print(b)

