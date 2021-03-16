import itertools as it

def solution(n):
    wm =['수','박']
    answer = []
    g = it.cycle(wm)
    for i in range(n):
        answer.append(g.__next__())
    return ''.join(answer)

print(solution(4))

print(int('-12312'))