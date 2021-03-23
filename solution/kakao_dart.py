def solution(dartResult : list):
    answer = 0
    score = {1 : ['','',''], 2 : ['','',''], 3 : ['','','']}

    c = ''
    currentKey = 1
    for i in range(len(dartResult)):
        tmp : str = dartResult[i]
        if tmp.isnumeric():
            score[currentKey][0] += tmp
        else:
            if tmp in ['S','D','T']:
                score[currentKey][1] += tmp
            else:
                score[currentKey][2] += tmp
            
            if currentKey < 3 and dartResult[i+1].isnumeric():
                currentKey += 1

    #print(score)

    for i in range(1,4):
        point = 0
        if score[i][1] == 'S':
            point = int(score[i][0])
        elif score[i][1] == 'D':
            point = int(score[i][0])**2
        else:
            point = int(score[i][0])**3
        
        if i < 3:
            if score[i+1][2] == '*':
                point *= 2
            if score[i][2] == '*':
                point *= 2
            elif score[i][2] == '#':
                point *= -1   
        else:
            if score[i][2] == '*':
                point *= 2
            elif score[i][2] == '#':
                point *= -1
            
        answer += point

    
    return answer


print(solution("1S2D*3T"))

print(solution("1D2S#10S"))