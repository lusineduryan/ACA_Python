numbers = (1,2,3)

a, b, c = numbers
print(a)
print(b)
print(c)

x, *y, z = [1,2,3,4,5,6,7]
print(x)
print(y)
print(z)

a = 2
b = 1 if a >= 5 else 42
print(b)

for i in range(10):
    if i == 999:
        break
else:
    print('1')