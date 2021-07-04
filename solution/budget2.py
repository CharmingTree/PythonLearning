
def solution(lst : list, budget):
    answer = 0

    lst.sort()

    maxSub = 0
    for i in range(len(lst)):
        temp = 0
        temp_cnt = 0
        for j in range(i, len(lst)):
            if temp + lst[j] <= budget:
                temp += lst[j]
                temp_cnt += 1
        
        if maxSub < temp_cnt:
            maxSub = temp_cnt



    return maxSub


print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))
