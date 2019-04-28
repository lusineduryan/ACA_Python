input_number = input()

even_pos = input_number[::2]
odd_pos = input_number[1::2]

print(sum(map(int, even_pos)) == sum(map(int, odd_pos)))