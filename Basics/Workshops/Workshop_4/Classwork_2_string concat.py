input_string = input()
concat = int(input())

if concat > 0:
    print(input_string * concat)
elif concat < 0:
    if input_string.count(input_string[0]) < abs(concat):
        print("undefined")
    else:
        input_string_order = input_string.find(input_string[0], len(input_string) // abs(concat) - 1)
        print(input_string[:input_string_order])