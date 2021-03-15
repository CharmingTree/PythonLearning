def solution(a, b):
    answer = 0
    if a == b : return 0
    return sum(range(a,b+1)) or sum(range(b, a+1))


print(solution(5,3))