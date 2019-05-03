# The input consists of two positive integers a and b, such that a<= b.
# Among the integers in the interval [a, b], find the one that has the most number of divisors.

range_start = int(input())
range_end = int(input())

max_count = 0
max_div_number = range_start

for i in range(range_start, range_end + 1):
    count = 0
    for j in range(1, i):
        if i % j == 0:
            count += 1
    if count > max_count:
        max_count = count
        max_div_number = i

print(max_div_number)
