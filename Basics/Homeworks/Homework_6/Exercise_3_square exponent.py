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

print(square_exp(2,10))

def square_exp_2(x, n):
    if n % 2 == 0:
        return (x ** (n/2)) ** 2
    else:
        return x * (x ** ((n-1)/2)) ** 2


print(square_exp_2(2,10))

print(2 ** 10)

