try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("An error occured")

try:
    x = 10
    print(x + "Hello")
except ZeroDivisionError:
    print("Divided by 0")
except(ValueError, TypeError):
    print("Error occured")

try:
    word = "spam"
    print(word / 0)
except:
    print("Error")
finally:
    print("This code will run no matter what")

name = "123"
raise NameError("Invalid name!")

try:
    num = 5 / 0
except:
    print("Error occured")
    raise

assert 2 + 2 == 4
assert 2 + 1 == 6, "invalid sum"

try:
    assert 2 + 2 == 5
except AssertionError:
    print("Invalid sum!")