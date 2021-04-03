
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

def fibo_iterator(n):
    if n < 2:
        return n
    temp = 0
    current = 1
    last = 0
    for i in range(2,n+1):
        temp = current
        current += last
        last = temp
    return current

print(fibo_iterator(1))
print(fibo_iterator(2))
print(fibo_iterator(3))
print(fibo_iterator(4))
print(fibo_iterator(5))

print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))