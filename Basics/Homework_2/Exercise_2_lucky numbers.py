# Call a number lucky if the sum of its digits on even positions is equal to the sum of its digits on odd positions.
# Given a number in decimal system(base 10): a. It’s length is 5 digits. Output True if a is lucky, otherwise False.

input_number = input()

int_number_coll = (int(input_number[0]), int(input_number[1]), int(input_number[2]), int(input_number[3]), int(input_number[4]))

print(sum(int_number_coll[::2]) == sum(int_number_coll[1::2]))



