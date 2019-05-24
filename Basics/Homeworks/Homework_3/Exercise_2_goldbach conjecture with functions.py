# The Goldbach’s Conjecture states that any positive even integer greater than two can be written as a sum of two primes.
# Given a positive even n not exceeding 10000, output two prime numbers such that their sum equals n.

input_number = int(input())

def isPrime (arg):
    for i in range(2, arg + 1):
        flag = True
        if arg % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
    return flag

for i in range(2, input_number + 1):
    if isPrime(i) == True and isPrime(input_number - i) == True:
        print(i, input_number - i)
        break
