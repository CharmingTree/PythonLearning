import collections

lst = ['a','b','c','d']

rs = collections.Counter(lst)

#print(rs)

#print(type(rs))

nums = [4,3,1,2]

sorted(nums)


nums.sort()

#print(nums)

#print(min(nums))


num = 1234

#for i in str(num):
#    print(i)


def solution(arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        answer.append([])
        for x in range(len(j)):  
            answer[-1].append(i[x]+j[x])
    return answer


def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    print(answer)
    return answer

solution([[1,2],[2,3]],[[3,4],[5,6]])


sumMatrix([[1,2],[2,3]],[[3,4],[5,6]])