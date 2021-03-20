import copy
def solution2(d, budget):
    pSetSize = 2**len(d)
    d_size = len(d)
    found = []
    d_sum = sum(d)

    if d_sum <= budget:
        return d_size

    av = d_sum // d_size
    temp = copy.copy(d)
    d = [i for i in range(d_size) if av <= temp[i]]

    pSetSize = 2**len(d)
    d_size = len(d)

    #print(d)

    d = sorted(d)
    for i in reversed(range(pSetSize)):
        flag = bin(i)[2:].zfill(d_size)
        #if len(found) >= 0
        subset = [d[j] for j in reversed(range(d_size)) if flag[j] == '1']
        subset_len = len(subset)
        subSum = sum(subset)
        #print(subset, subSum)
        if subSum <= budget:
            found.append(subset_len)
            #print(found[-1])
            break
    result = max(found)

    return result


def solution(d, budget):
    pSetSize = 2**len(d)
    d_size = len(d)
    found = []

    if sum(d) <= budget:
        return d_size
    d = sorted(d)
    for i in reversed(range(pSetSize)):
        flag = bin(i)[2:].zfill(d_size)
        subset = [d[j] for j in reversed(range(d_size)) if flag[j] == '1']
        subset_len = len(subset)
        subSum = sum(subset)
    
        if subSum <= budget:
            found.append(subset_len)
            #print(subset, subSum)
            break
    result = max(found)

    return result


print(solution([1,3,2,5,4],9))


print(solution([2,2,3,3],10))






