# User inputs string like this ‘486+210’ where first 3 characters are numbers, 4th is sign which is always plus, and last 3 characters are also numbers. Compute and return value of expression.
# Example: ‘486+210’ return 696
# Example: ‘120+044’ return 164

input_number = input()

int_number_1 = int(input_number[:3])
int_number_2 = int(input_number[-3:])

print(int_number_1 + int_number_2)