def solution(numbers):
    
    map = set()
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            ad = numbers[i] + numbers[j]
            map.add(ad)

    answer = list(map)
    return answer



#result = solution([2,1,3,4,1])
result = solution([3,4,5,6,7])

print(result)
