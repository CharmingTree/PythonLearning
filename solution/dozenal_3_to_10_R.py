import math

def dz3(n, f : list):
    q = 0
    r = 0
    if n < 3:
        f += str(n)
        return f
    else:
        q = n // 3
        r = n % 3
        f += str(r)
        dz3(q, f)


def solution(n):
    answer = 0
    t = []
    dz3(n, t)
    nuberic = list(str(int(''.join(t))))
    nuberic.reverse()
    for i in range(len(nuberic)):
        answer +=  math.pow(3,i) * int(nuberic[i])
    return int(answer)


solution(45)

