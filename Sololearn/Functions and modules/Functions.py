def my_func():
    print("Hi")

my_func()

def print_with_exclamation(word):
    print(word + "!")

print_with_exclamation("Lucy")

def print_sum(x, y):
    print(x + y)

print_sum(5, 15)

def max_number(x, y):
    if x >= y:
        return x
    else:
        return y

a = max(5, 23)
print(a)

def multiply(x, y):
    return x * y

operation = multiply
print(operation(5, 6))

def add(x, y):
  return x + y
def do_twice(f, x, y):
    return f(f(x, y), f(x, y))
print(do_twice(add, 7, 3))