# Output all the prime multiplers of the given number and the degrees.

k = int(input())

count_2 = 0
t = k
while t % 2 == 0:
    count_2 += 1
    t /= 2

print(2, count_2)

for i in range(3, k, 2):
    count = 0
    while k % i == 0:
        count += 1
        k /= i
    if count != 0: print(i, count)