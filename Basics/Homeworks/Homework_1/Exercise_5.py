# Add two unsigned integers of length 3(bits) using their binary representation.

input_number_1 = input()
input_number_2 = input()

int_number_1 = int(input_number_1, base = 2)
int_number_2 = int(input_number_2, base = 2)

print(bin((2 ** 0) * (int_number_1 // 2 ** 0 % 2 + int_number_2 // 2 ** 0 % 2) + \
          (2 ** 1) * (int_number_1 // 2 ** 1 % 2 + int_number_2 // 2 ** 1 % 2) + \
          (2 ** 2) * (int_number_1 // 2 ** 2 % 2 + int_number_2 // 2 ** 2 % 2)))

