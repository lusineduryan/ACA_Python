import random

def prob_of_match():
    pos = [1,2,3]
    number_of_exp = 100000
    res = 0
    for i in range(number_of_exp):
        random.shuffle(pos)
        res += any(map(lambda a, b: a == b, pos, range(1, 4)))
    return res / number_of_exp

print(prob_of_match())