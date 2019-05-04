 # The Goldbach’s Conjecture states that any positive even integer greater than two can be written as a sum of two primes.
# Given a positive even n not exceeding 10000, output two prime numbers such that their sum equals n.

input_number = int(input())

primes = []
for i in range(2, input_number + 1):
    bool = True
    for j in range(2, i):
        if i % j == 0:
            bool = False
            break
    if bool == True: primes.append(i)

for i in primes:
    if input_number - i in primes:
        print(i, input_number - i)
        break
