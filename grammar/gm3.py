price = ['20210310', 1,2,3,4,5]



result = [i for i in price if type(i) == int]

print(result)

print(price[1:])


numbers = [1,2,3,4,5,6]

print(numbers[::2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))

string = "삼성전자/LG전자/Naver"

print(string.split('/'))

## [] = list, {} = dic, () = tuple
my_tuple = ()
print(type(my_tuple))

my_tuple = ('아저씨', '신세계', '범죄도시')

print(my_tuple)

num_tuple = (1,)

print(num_tuple)

t = 'A', 'B', 'C'

print(t, " ", type(t))

t = 'a','b','c'


print(t, " ", type(t))


trans_list = [i for i in t]

print(trans_list, type(trans_list))
## or
print(list(t))

print(tuple(trans_list))

fruits = 'apple', 'banana', 'charry'

a, b, c = fruits

print(a,b,c)

d = None

gg = d == None and 'a' or 'b'
cc = 'g' if d == None else 'b'

print(cc)


ab = tuple(range(2,100,2))

print(ab)


a, b, *c= (1,2,3,4,5,6)

print(a,b,c)

## 좌측 8개 바인딩하기
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*newbinding, _, _ = scores

print(newbinding)

## 우측 8개 바인딩

_, _, *right_binding = scores

print(right_binding)

_, *mid_binding, _ = scores

print(mid_binding)

ice_cream = {'merona': 1000, 'bbangbalea': 2000, 'summer_hunting' : 1999}
print(ice_cream)

ice_cream['죠스바'] = 3000

print(ice_cream)

print(ice_cream['merona'])

ice_cream['merona'] = 2000

print(ice_cream['merona'])

print(ice_cream.pop('merona'))

print(ice_cream)


ice_cream = {'merona' : [300, 20], 'bbangppalea' : [200, 10]}

print(ice_cream)

print(ice_cream['merona'][0])

ice_cream['worldcon'] = [140, 10]

print(ice_cream)

ice = list(ice_cream.keys())
print(ice)

ice_value = list(ice_cream.values())

print(ice_value)

sums = [j for i in list(ice_cream.values()) for j in i]

print(sums)


def solution(a, b):
    if a > b:
        a ,b = b, a
    answer = 0
    for i in range(a,b):
        answer += i
    return answer


def solution(n, lost, reserve):
    # n 전체학생
    # lost 도난당한 학생 체육복 번호
    # 여벌의 체육복을 가진 학생 번호
    check = {}
    for i in reserve:
        check.setdefault(i,True)
        print(check)
    dc = len(lost)
    for i in lost:
        print("i >>>> ", i )
        for j in range(i-1,i+2):
            if check.get(j) is not None and check[j] == True:
                print("00000000  ", j)
                dc -= 1
                check[j] = False
                break
    
    return n-dc


result = solution(3, [1,2], [1,3,5])
print(result)


def solution2(n):
    
    a = [False,False] + [True]*(n-1)
    result = []

    for i in range(2,n+1):
        if a[i]:
            result.append(i)
            for j in range(2*i,n+1,i):
                a[j] = False
    print(result)
    return len(result)

print(solution2(100))

