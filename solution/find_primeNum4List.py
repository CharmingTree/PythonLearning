import math
import time

def solution2(nums):
    answer = 0
    primeCnt = 0 

    powerSet = []

    a_size = len(nums)
    for i in range(2**a_size):
        flag = bin(i)[2:].zfill(a_size)
        subset = [nums[j] for j in range(a_size) if flag[j] == '1']
        if len(subset) == 3:
            powerSet.append(sum(subset))
    
    maxNum = max(powerSet)

    primes = [False,False] + [True] * (maxNum-1)
    pNumList = []
    for i in range(2,len(primes)):
        if primes[i]:
            pNumList.append(i)
            for j in range(2*i, len(primes),i):
                primes[j] = False

    for i in range(len(powerSet)):
        if powerSet[i] in pNumList:
            answer += 1

    return answer





def solution(nums):
    answer = 0
    primeCnt = 0 

    powerSet = []

    a_size = len(nums)
    print(2**a_size)
    print(bin(4)[2:].zfill(a_size))

    start = time.time()
    for i in range(2**a_size):
        flag = bin(i)[2:].zfill(a_size)
        subset = [nums[j] for j in range(a_size) if flag[j] == '1']
        if len(subset) == 3:
            powerSet.append(sum(subset))
    
    print("WorkingTime: {} sec".format(time.time() - start))
    maxNum = max(powerSet)

    primes = [True for i in range(maxNum+1)]
    
    for i in range(2, int(math.sqrt(maxNum))+1):
        if primes[i]:
            j = 2
            while i * j <= maxNum:
                primes[i * j] = False
                j += 1

    primeList = [ i for i in range(2, maxNum+1) if primes[i]]    

    for i in range(len(powerSet)):
        if powerSet[i] in primeList:
            answer += 1
    return answer

print(solution([1,2,3,4,8,10,11,13,15,19,20,21,22,23,24,25,27,100,42]))
