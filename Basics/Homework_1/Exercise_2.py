# Write Program which will set a-th bit of a given number to 1. (Counting from lower order to higher).

input_number_1 = input()
input_number_2 = input()

int_number_1 = int(input_number_1, base = 2)
int_number_2 = int(input_number_2)

print(int_number_1 + (1 - int_number_1 // 2 ** int_number_2 % 2) * 2 ** int_number_2)

