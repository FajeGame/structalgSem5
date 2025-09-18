import time

def foo(n): # n - число
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1   
            j += 1
        if divisors == 0:
            res.append(i)
    return res

h = 1000
u = 0
for i in range(0, 20):
    start_time = time.time()
    foo(h)
    end_time = time.time()
    elapsed_time = end_time - start_time
    u += 1
    print('Время выполнения', u, '(', h, ')', ': ', elapsed_time)
    h += 1000