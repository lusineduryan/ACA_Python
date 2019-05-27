fact = {0: 1}

def factorial(n):
    if n not in fact:
        fact[n] = factorial(n - 1) * n
    return fact[n]

print(factorial(int(input())))
