squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(squares[2:6])
print(squares[:5])
print(squares[5:])

print(squares[2:8:3])
print(squares[::2])

print(squares[1:-1])


cubes = [i ** 3 for i in range(5)]
print(cubes)

evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)