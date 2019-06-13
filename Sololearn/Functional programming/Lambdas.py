def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2 * x, 5))

print((lambda x: x ** 2)(5))

triple = lambda x: x * 3
print(triple(7))