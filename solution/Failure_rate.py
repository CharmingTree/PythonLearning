
# 5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 
def solution(N, stages):
    answer = []
    #stageSet = sorted(list(set(stages)))
    #print(stageSet)
    remained_user = len(stages)
    statusMap = {}
    failureRate = {}
    for i in range(1,N+1):
        statusMap.setdefault(i,0)
        failureRate.setdefault(i,0)
        for j in range(len(stages)):
            if i == stages[j]:
                statusMap[i] += 1
    
    
    for i in range(1,N+1):
        if remained_user == 0:
            break
        failureRate[i] = statusMap[i]/remained_user
        remained_user -= statusMap[i]

    answer = [i[0] for i in sorted(failureRate.items(), key = lambda x : x[1],reverse=True)]

    return answer


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))

print(solution(4, [4, 4, 4, 4, 4]))