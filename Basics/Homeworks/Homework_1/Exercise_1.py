# find the number of 1-s in a 5-digit number

input_number = input()

int_number = int(input_number, base = 2)

print(int(int_number >= 2**4) + \
      int(int_number % 2**4 >= 2**3) + \
      int(int_number % 2**3 >= 2**2) + \
      int(int_number % 2**2 >= 2**1) + \
      int(int_number % 2**1 >= 2**0))

