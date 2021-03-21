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


def getBit(num):
    cnt = 0

    while num != 0:
        num = num & (num -1)
        cnt += 1
    
    return cnt


def solution(nums):
    answer = 0

    a_size = len(nums)
    nums.sort()

    maxSum = 0
    for i in nums[-3:]:
        maxSum += i

    primes = [True for i in range(maxSum+1)]
    
    for i in range(2, maxSum+1):
        if primes[i]:
            j = 2
            while i * j <= maxSum:
                primes[i * j] = False
                j += 1
    for i in range(a_size):
        for j in range(i+1, a_size):
            for k in range(j+1, a_size):
                tmp = nums[i] + nums[j] + nums[k]
                if primes[tmp]:
                    answer += 1
    # for i in range(2**a_size):
    #     if getBit(i) != 3:
    #         continue
    #     flag = bin(i)[2:].zfill(a_size)
    #     tmp = sum([nums[j] for j in range(a_size) if flag[j] == '1'])
    #     if primes[tmp]:
    #         answer += 1

    return answer

print(solution([1,2,3,4,8,10,11,13,15,19,20,21,22,23,24,25,27,100,42]))
print(solution([1,2,3,4,8]))

def solution3(nums):
    answer = 0
    primeCnt = 0 

    powerSet = []

    a_size = len(nums)
    for i in range(2**a_size):
        flag = bin(i)[2:].zfill(a_size)
        subset = [nums[j] for j in range(a_size) if flag[j] == '1']
        if len(subset) == 3:
            tmp = sum(subset)
            if tmp % 2 == 0 or tmp % 3 == 0 or tmp % 5 == 0:
                continue
            else:
                powerSet.append(tmp)
    
    maxNum = max(powerSet)

    primes = [True for i in range(maxNum+1)]
    
    for i in range(2, int(math.sqrt(maxNum))+1):
        if primes[i]:
            j = 2
            while i * j <= maxNum:
                primes[i * j] = False
                j += 1

    for i in range(len(powerSet)):
        if primes[powerSet[i]] :
            answer += 1
    return answer