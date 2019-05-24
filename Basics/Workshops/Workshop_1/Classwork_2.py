# find the number of 1-s in a 5- number

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

print("Count: ", count)
