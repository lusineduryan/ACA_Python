def bin_exp(x, k):
    res = 1
    n = 2 ** k
    while n > 0:
        n = n / 2
        x = x * x
        res = res * x
    return res

print(bin_exp(2,100))