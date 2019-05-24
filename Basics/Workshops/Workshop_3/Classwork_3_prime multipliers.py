# Output all the prime multiplers of the given number and the degrees.

k = int(input())

A = []
for i in range(2, k + 1):
    bool = True
    if k % i == 0:
        for j in range(2, i):
            if i % j == 0:
                bool = False
                break
        if bool == True: A.append(i)

print(A)
for i in A:
    m = k
    count = 0
    while m % i == 0:
        count += 1
        m /= i
    print(f'({i}, {count})')
