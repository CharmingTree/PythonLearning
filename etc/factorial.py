

def fact(n):
    if n <= 1:
        return n
    else:
        return n * fact(n-1)

def fact_iterator(n):
    if n <= 1:
        return n
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret


print(fact(5))
print(fact_iterator(5))