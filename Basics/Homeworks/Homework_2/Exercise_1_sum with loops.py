import time

start = time.perf_counter()

a_i = 0
d = 5
res = 0

for i in range(1, 1001, 1):
    a_i = a_i + i % 3 * d
    res += a_i

print(res)

print(time.perf_counter() - start)

