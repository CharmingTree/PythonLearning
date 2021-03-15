def solution(arr, divisor):
    answer = []

    print(len(answer))
    
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])

    if len(answer) != 0:
        answer.sort()
    else:
        answer.append(-1)
    # answer = sorted(answer) if len(answer) != 0 else answer.append(-1)
    
    return answer



print(solution(	[3, 2, 6], 10))