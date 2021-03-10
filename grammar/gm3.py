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