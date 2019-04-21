# Find the sum of a sequence, where a_i = a_i-1 + i % 2 * d, i = [0:1000]

a_0 = 1
d = 5
a_1 = a_0 + 1 % 2 * 5
end = a_1 + 500 * d
range_half = range(a_1, end, d)
print(2 * sum(range_half) + a_0)