# Print the remainder of the division of the factorial for the given natural number and a prime number.

k = int(input())
p = 7

if k >= p: f = 0
else:
    f = 1
    for i in range(1, k + 1):
        m = i % p
        f *= m

print(f % p)