import time

def square_exp(x, n):
    res = 1
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            x = x * x
        else:
            n = n - 1
            res = res * x
            n = n / 2
            x = x * x
    return res

print(square_exp(2,101))

def square_exp_2(x, n):
    if n % 2 == 0:
        return (x ** (n/2)) ** 2
    else:
        return x * (x ** ((n-1)/2)) ** 2

def square_exp_3(x, n):
    return x ** n

print(square_exp_2(2,101))

print(2 ** 101)

start1 = time.perf_counter()
square_exp(2,101)
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
square_exp_2(2,101)
time2 = time.perf_counter() - start2

start3 = time.perf_counter()
square_exp_3(2,101)
time3 = time.perf_counter() - start3

print(time2 > time3)