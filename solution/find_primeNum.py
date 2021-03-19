def solution(n):
    num = [False,False] + [True]*(n-1)
    primeNum = []
    for i in range(2,n+1):
        if num[i]:
            primeNum.append(i)
            for j in range(2*i, n+1, i):
                num[j] = False
    print(len(num), num)
    return len(primeNum)

solution(100)

