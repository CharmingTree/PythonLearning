# 반복가능 객체 list, dic, tuple, range, set, file

# 반복 가능 객체인지 검사

try:
    l = [10,20,30]
    iterator = iter(l)
    iterator.__next__()
    iterator.__next__()
    iterator.__next__()
    iterator.__next__()

except StopIteration:
    print("StopIterator")
    
except TypeError:
    print("반복가능 객체가 아닙니다")
else:
    print("반복가능 객체 입니다.")


try:
    l = (10,20,'kangjunyoung')
    iterator = iter(l)
except TypeError:
    print("반복가능 객체가 아닙니다")
else:
    print("반복가능 객체 입니다")

try:
    n = 100
    iterator = iter(n)
except TypeError:
    print("반복가능 객체가 아닙니다")
else:
    print("반복가능 객체 입니다")


class oddCounter:
    def __init__(self, n = 1):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < 30: 
            t = self.n
            self.n += 2
            return t
        raise StopIteration


myCnt = oddCounter()

for i in myCnt:
    print(i, end = ' ')


try:
    f = open('./asset/a.txt')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(f)
    f.close()


a = [1,2,3,4]

print(id(a))

a = a + [5]

print(id(a))