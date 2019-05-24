def dict_gen():
    dict = {}
    f = 1
    for i in range(1, 100):
        f *= i
        dict[i] = f
    return dict

def factorial(n, dict):
    if n not in dict:
        max_member = max(dict)
        fact = dict[max_member]
        for i in range(max_member + 1, n + 1):
            fact *= i
        dict[n] = fact
    return dict[n]

print(factorial(int(input()), dict_gen()))