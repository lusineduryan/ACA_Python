# Add two unsigned integers of length 3(bits) using their binary representation.

input_number_1 = input()
input_number_2 = input()

int_number_1 = int(input_number_1, base = 2)
int_number_2 = int(input_number_2, base = 2)

a_0 = int_number_1 % 2
b_0 = int_number_2 % 2
a_1 = int_number_1 // 2 % 2
b_1 = int_number_2 // 2 % 2
a_2 = int_number_1 // 2 ** 2 % 2
b_2 = int_number_2 // 2 ** 2 % 2

c_0 = (a_0 + b_0) % 2
accm = (a_0 + b_0) // 2
c_1 = (a_1 + b_1 + accm) % 2
accm = (a_1 + b_1 + accm) // 2
c_2 = (a_2 + b_2 + accm) % 2
accm = (a_2 + b_2 + accm) // 2
c_3 = accm

print(c_3, c_2, c_1, c_0)