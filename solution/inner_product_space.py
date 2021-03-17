import math

def solution(a, b):
    answer = 0
    for i, j in zip(a,b):
        answer += i*j
    return answer

# print(solution([1,2,3], [2,4,3]))

f = 'asdad asdd '

#print(f.split(' '))

def solution2(n):
    answer = 0
    a = 10
    for i in range(len(str(n))):
        answer += n % a
        n //= a
    return answer

# print(solution2(123))


print(math.sqrt(121))

print(1.7%1)
