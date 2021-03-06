

ages = [10, 11, 23, 40]

# 자바 스트림이랑 비슷하게 사용가능 하다.
adult_age = list(filter(lambda x : x >= 19, ages))

print(adult_age)

print(' adult_age_list : ', [x for x in ages if x >= 19])

numList = [-23,-32,0, 33, 12, 23, 90, 1, 11,22, 19, -4, 5]

minusNum = list(filter(lambda x : x < 0, numList))

print('numList : ', minusNum)

print('list express : ', [x for x in numList if x < 0])


# 2차원 배열 리스트 축약 표현으로 실습
product_xy = []

for i in range(1,5):
    for j in range(1,3):
        product_xy.append(i*j)


print(product_xy)


product_xy = [ x * y for x in range(1,5) for y in range(1,3)]

print(product_xy)

def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}
    return res


A = {1, 2, 3}
B = [19, 0 , 2]

AUB = product_set(A,B)

print(A)
print(B)
print(AUB)

# 축약표현으로 합집합 표현 
def contraction_product_set(set1, set2):
    return {(i,j) for i in set1 for j in set2}

print(contraction_product_set(A,B))

# 주사위를 두번 던져서 나올 수 있는 경우의 수 

cases = [1,2,3,4,5,6]

allCases = contraction_product_set(cases, cases)

print(allCases)

# 주사위를 두번 던져서 나올 수 있는 경우의 수 합

sum_set = { sum(tup) for tup in allCases}
print('sumset \n', sum_set)

sum_list = [sum(tup) for tup in allCases]
print('sum_list \n',  sum_list)


# 주사위를 세번 던져서 나올 수 있는 경우의 수 합 
def tuple_sum(tup):
    if isinstance(tup, int):
        return tup
    else:
        accum = 0
        for i in tup:
            accum += tuple_sum(i)
    return accum


case_times2 = contraction_product_set(cases, cases)
case_times3 = contraction_product_set(cases, case_times2)

sums = {tuple_sum(s) for s in case_times3}

caselen = [tuple_sum(s) for s in case_times3]
print(len(caselen))


print("주사위를 3번 던져서 10 이상이 나올수 있는 경우의 수는 ", len([x for x in caselen if x >= 10]))
