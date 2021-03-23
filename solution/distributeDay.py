def solution(progresses, speeds):
    answer = []

    d_day = []
    for i in range(len(progresses)):

        s = sum([1 for j in range(progresses[i], 100, speeds[i])])
        d_day.append(s)
    
    print(d_day)
    return answer

solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
