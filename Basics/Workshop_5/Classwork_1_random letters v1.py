import random

def letter_match():
    res = 0
    number_of_exp = 10000
    for i in range(number_of_exp):
        first_letter = random.randint(1, 3)
        second_letter = random.randint(1, 3)
        if second_letter == first_letter:
            second_letter = random.randint(1, 3)
        third_letter = random.randint(1, 3)
        if third_letter == first_letter or third_letter == second_letter:
            third_letter = random.randint(1, 3)
        if first_letter == 1 or second_letter == 2 or third_letter == 3:
            res += 1
    return res / number_of_exp

print(letter_match())

