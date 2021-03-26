def solution(priorities, location : int):
    answer = 0
    s = []
    result = []
    for i in range(len(priorities)):
        s.append([i, priorities[i]])

    while len(s) != 0:
        tmp = s[0]
        for i in range(1, len(s)):
            if s[0][1] < s[i][1]:
                s.append(s.pop(0))
                break
        if tmp == s[0]:
            result.append(tmp)
            s.pop(0)
    
    for i in range(len(result)):
        if result[i][0] == location:
            answer = i+1
            break
    
    return answer





print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
print(solution([1, 1, 9, 1, 1, 3, 1, 1], 4))

# 9 1 1 1 1 1