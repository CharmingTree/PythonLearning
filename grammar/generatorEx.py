gt = (x for x in range(100))

for i in gt:
    print(i)

print(type(gt))

import time

def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# start_t = time.time()

# for x in fibon(100000):
#     pass

# end_t = time.time()
# print('total time = ', end_t - start_t)


def fibon_with_yield(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

start_t = time.time()

for x in fibon_with_yield(1000000):
    pass

end_t = time.time()

print('total time = ', end_t - start_t)