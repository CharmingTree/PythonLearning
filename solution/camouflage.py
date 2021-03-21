
def solution(clothes):
    answer = 0
    cMap = {}

    for i in range(len(clothes)):
        if clothes[i][1] not in cMap:
            cMap.setdefault(clothes[i][1], [clothes[i][0]])
        else:
            cMap.get(clothes[i][1]).append(clothes[i][0])
    
    isWorseCase = True

    

    vList = list(cMap.values())
    for i in range(len(vList)):
        if len(vList[i]) != 1:
            isWorseCase = False
            break 
    
    # if isWorseCase:
    #     return 2**len(vList)-1

    keys = list(cMap.keys())
    keySize = len(keys)
    powerSet = []

    for i in range(1,2**keySize):
        flag = bin(i)[2:].zfill(keySize)
        subSet = [keys[j] for j in range(keySize) if flag[j] == '1']
        t = 1
        for j in range(len(subSet)):
            t *= len(cMap[subSet[j]])
        answer += t
        #powerSet.append(subSet)
    
    # for i in range(len(powerSet)):
    #     print(powerSet[i])
    #     t = 1
    #     for j in range(len(powerSet[i])):
    #         t *= len(cMap[powerSet[i][j]])
    #     answer += t
    return answer



#print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([['1','a'],['1','b'],['1','c'],['1','d']]))
# print(solution(
#     [["crowmask", "face"],
#      ["bluesunglasses", "face"],
#      ["smoky_makeup", "face"],
#      ["yellowhat", "headgear"],
#      ["bluesunglasses", "eyewear"],
#      ["green_turban", "headgear"],
#      ["aaaaaa","eyewear"],
#      ["bbbbbbb", "headgear"]
#      ]))


## 1 2
## 3 4
## 5 6