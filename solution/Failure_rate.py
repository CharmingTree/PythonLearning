
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
    
    for i in range(1,N):
        failureRate[i] = statusMap[i]/remained_user
        remained_user -= statusMap[i]
        print('remained User : ', remained_user)

    for key, value in sorted(failureRate.items()):
        print(key, value)
    
    print(statusMap)
    return answer


solution(5,[2, 1, 2, 6, 2, 4, 3, 3])