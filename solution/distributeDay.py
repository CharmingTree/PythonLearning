import math
def solution(progresses, speeds):
    answer = []
    d_day = []   
    for i in range(len(progresses)):
        t = math.ceil((100-progresses[i]) / speeds[i])
        d_day.append(t)
    target = d_day[0]
    tmp = []
    while len(d_day) != 0:
        if target >= d_day[0]:
            tmp.append(d_day.pop(0))
        else:
            target = d_day[0]
            answer.append(len(tmp))
            tmp = []
            continue
    if len(tmp) != 0:
        answer.append(len(tmp))

    return answer

solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
