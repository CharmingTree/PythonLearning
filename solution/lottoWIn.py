def solution(lottos : list, win_nums : list):
    answer = []

    score = 0
    lostCnt = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            score += 1
            continue
        if lottos[i] == 0:
            lostCnt += 1
    
    # print(score)
    # print(lostCnt)

    result = [score+lostCnt, score]

    for i in range(2):
        if result[i] == 6:
            answer.append(1)
        elif result[i] == 5:
            answer.append(2)
        elif result[i] == 4:
            answer.append(3)
        elif result[i] == 3:
            answer.append(4)
        elif result[i] == 2:
            answer.append(5)
        else:
            answer.append(6)

    return answer


print (solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))