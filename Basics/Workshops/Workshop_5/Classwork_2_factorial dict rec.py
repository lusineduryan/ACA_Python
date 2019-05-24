fact = {0: 1}

def factorial(n):
    if n in fact:
        return fact[n]
    else:
        fact[n] = factorial(n - 1) * n
        return fact[n]

print(factorial(int(input())))
