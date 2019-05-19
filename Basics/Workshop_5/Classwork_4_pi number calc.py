import random

def pi():
    number_of_exp = 100000
    R = 1
    inside_points = 0
    for i in range(number_of_exp):
        x_axis = random.random()
        y_axis = random.random()
        if x_axis ** 2 + y_axis ** 2 < R ** 2:
            inside_points += 1
    return 4 * inside_points / number_of_exp

print(pi())