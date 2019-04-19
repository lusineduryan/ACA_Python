# Add two unsigned integers of length 3(bits) using their binary representation.

input_number_1 = input()
input_number_2 = input()

int_number_1 = int(input_number_1, base = 2)
int_number_2 = int(input_number_2, base = 2)

bin_number_1 = bin(int_number_1)
bin_number_2 = bin(int_number_2)

sum = int_number_1 + int_number_2
print(bin(sum))