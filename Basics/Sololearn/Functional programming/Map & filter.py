def add_two(arg):
    return arg + 2

nums = [11, 22, 33, 44, 55]

print(list(map(add_two, nums)))

print(list(filter(lambda x: x % 2 == 0, nums)))