def solution(numbers):
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
        for i in range(1, pSetSize):
            flag = bin(i)[2:].zfill(len(numbers))
            bucket.add(int(''.join([numbers[x] for x in range(len(numbers)) if flag[x] == '1'])))

    bucket = sorted(list(bucket))
    print(bucket)
    primes = [True for i in range(bucket[-1]+1)]
    
    for i in range(2, bucket[-1]+1):
        if primes[i]:
            j = 2
            while i * j <= bucket[-1]:
                primes[i * j] = False
                j += 1
    for i in range(len(primes)):
        print(i, primes[i])
    for i in range(len(bucket)):
        if bucket[i] > 1:
            if primes[bucket[i]]:
                answer += 1 
    
    return answer

print(solution("17"))


print(solution("123"))

