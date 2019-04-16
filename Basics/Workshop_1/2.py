number = int(input(), base=2)
result = number // 2**0 % 2 + \
         number // 2**1 % 2 + \
         number // 2**2 % 2 + \
         number // 2**3 % 2 + \
         number // 2**4 % 2
print(result)
