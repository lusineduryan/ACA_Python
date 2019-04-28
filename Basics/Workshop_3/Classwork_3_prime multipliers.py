k = int(input())

A = []
count = 0
for i in range(2, k + 1):
    bool = True
    if k % i == 0:
        for j in range(2, i):
            if i % j == 0:
                bool = False
                break;
        if bool == True: A.append(i)

print(A)
for i in A:
