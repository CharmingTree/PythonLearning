
from typing import KeysView


m1 = { 3 : 'a', 2 : 'b', 1 : 'c', 9999 : 'A'}

m2 = sorted(m1.items(), key= lambda x : x[1])


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [4, 1, 2, 3, 4, 5, 6, 8, 4, 32]
b = list(map(lambda x : str(x) if x % 3 == 0 else x, a))
c = list(map(lambda x : x if x == 1 else float(x) if x == 2 else x+10, a))
e = list(map(lambda x, y : x*y,a,d))


def f(x):
    if x < 10 and x > 5:
        return True
    else:
        return False

g = list(filter(f,a))
h = list(filter(lambda x : x < 10 and x > 5, a))


gggg = sorted(m1, key=m1.get)

print(gggg)



count = a.count(1)
