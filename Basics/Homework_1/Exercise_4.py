# Find remainder without using modulo operator

input_number_1 = input()
input_number_2 = input()

int_number_1 = int(input_number_1)
int_number_2 = int(input_number_2)

print(int_number_1 - int_number_2 * (int_number_1 // int_number_2))