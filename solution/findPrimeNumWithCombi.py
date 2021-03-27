
def list_Lshift(arr):
    front = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = front

def solution(numbers):
    answer = 0
    bucket = set()
    pSetSize = 2**len(numbers)

    for i in range(1, pSetSize):
        flag = bin(i)[2:].zfill(len(numbers))
        pSet = [numbers[x] for x in range(len(numbers)) if flag[x] == '1']
        bucket.add(int(''.join(pSet)))
        for j in range(len(pSet)-1):
            list_Lshift(pSet)
            print(pSet)
            bucket.add(int(''.join(pSet)))

    

    bucket = sorted(list(bucket))
    print(bucket)

    print(bucket[-1])
    primes = [True for i in range(bucket[-1]+1)]
    
    for i in range(2, bucket[-1]+1):
        if primes[i]:
            j = 2
            while i * j <= bucket[-1]:
                primes[i * j] = False
                j += 1
    for i in range(len(bucket)):
        if bucket[i] > 1:
            if primes[bucket[i]]:
                answer += 1 
    
    return answer


def solution2(numbers):

    numbers = list(numbers)
    numbers = sorted(numbers, reverse=True)
    numbers = ''.join(numbers)

    print(numbers)

    answer = 0
    bucket = set()
    pSetSize = 2**len(numbers)

    remain = numbers
    lock = True
    for k in range(len(numbers)):
        numbers += numbers[0]
        numbers = list(numbers)
        numbers.pop(0)
        numbers = ''.join(numbers)
        print(numbers)
        for i in range(1, pSetSize):
            flag = bin(i)[2:].zfill(len(numbers))
            bucket.add(int(''.join([numbers[x] for x in range(len(numbers)) if flag[x] == '1'])))

    bucket = sorted(list(bucket))

    print(bucket[-1])
    primes = [True for i in range(bucket[-1]+1)]
    
    for i in range(2, bucket[-1]+1):
        if primes[i]:
            j = 2
            while i * j <= bucket[-1]:
                primes[i * j] = False
                j += 1
    for i in range(len(bucket)):
        if bucket[i] > 1:
            if primes[bucket[i]]:
                answer += 1 
    
    return answer


#print(solution("17"))


#print(solution("123"))
#print(solution("235711"))

import itertools
aa = [1,1,3]

case = itertools.permutations(aa)

print(list(case))