def solution(left, right):
    answer = 0


    for i in range(left, right+1):
        cnt = 0

        j = 1
        while j*j <= i:
            if i % j == 0:
                cnt += 1
                if j * j < i:
                    cnt+=1
            j += 1

        if (cnt % 2 == 0):
            answer += i
        else:
            answer -= i

    return answer


print(solution(13, 17))