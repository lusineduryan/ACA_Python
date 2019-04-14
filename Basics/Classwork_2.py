input_number = input()

int_number = int(input_number, base = 2)

print(int_number)

count = 0

count += int_number % 2
int_number = int_number // 2

count += int_number % 2
int_number = int_number // 2

count += int_number % 2
int_number = int_number // 2

count += int_number % 2
int_number = int_number // 2

count += int_number

count_short = int_number % 2 + int_number // 2 % 2 + int_number // 4 % 2 + int_number // 8 % 2 + int_number // 16 % 2



print(count)
print(count_short)