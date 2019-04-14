input_number = input()

int_number = int(input_number, base = 2)

int_number_1 = int(input_number, base = 10)

print(int_number)
print(int_number_1)

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

count_short = int_number_1 % 2 + int_number_1 // 2 % 2 + int_number_1 // 4 % 2 + int_number_1 // 8 % 2 + int_number_1 \
              // 16 % 2



print("Count: ", count)
print("Count_short: ", count_short)