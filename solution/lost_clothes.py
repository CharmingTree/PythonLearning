def solution(n, lost: list, reserve: list):
    answer = n

    # 여분 소유자가 도난 리스트에 있으면 여분 리스트에서 제거
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -1
    
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -1
        elif (lost[i]-1) > 1 and (lost[i]-1) in reserve:
            reserve.remove((lost[i]-1))
            lost[i] = -1
        elif (lost[i]+1) <= n and (lost[i]+1) in reserve:
            reserve.remove((lost[i]+1))
            lost[i] = -1
    print('lost = ', lost)
    print('reserve = ', reserve)

    for i in range(len(lost)):
        if lost[i] != -1:
            answer -= 1

    return answer

result = solution(5, [1, 2, 4],	[1, 3, 5])
result = solution(5, [2, 4], [1, 3, 5])


print(result)