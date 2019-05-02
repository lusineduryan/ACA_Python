# Output all the prime multiplers of the given number and the degrees.

k = int(input())

count_2 = 0
while k % 2 == 0:
    count_2 += 1

print(2, count_2)

for i in range(3, k, 2):
    count = 0
    m = k
    while m % i == 0:
        count += 1
        m /= i
    print(i, count)