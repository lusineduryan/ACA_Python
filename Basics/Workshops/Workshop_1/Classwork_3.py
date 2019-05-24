#replace the ath digit of a number with 0 or 1

input_number_1 = input()
input_number_2 = input()

int_number_1 = int(input_number_1, base = 2)
int_number_2 = int(input_number_2, base = 10)


if int_number_1 // 2 ** int_number_2 % 2 == 0:
    print(int_number_1)
else:
    print(int_number_1 - 2 ** int_number_2)

if int_number_1 // 2 ** int_number_2 % 2 == 1:
    print(int_number_1)
else:
    print(int_number_1 + 2 ** int_number_2)
