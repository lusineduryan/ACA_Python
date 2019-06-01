def bin_exp(x, n):
    res = 1
    power = 2 ** n
    while power >= 2:
        power = power / 2
        x = x * x
    return x

def bin_exp_2(x, n):
    return (x ** n) ** 2

print(bin_exp(2,3))