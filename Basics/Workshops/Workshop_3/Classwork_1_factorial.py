# Print thr factorial for the given natural number.

input_number = int(input())

fact = 1
for i in range(1, input_number + 1, 1):
    fact *= i

print(fact)