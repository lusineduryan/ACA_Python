fact = {0: 1}

def factorial(n):
    if n in fact:
        return fact[n]
    else:
        return factorial(n - 1) * n

print(factorial(int(input())))
