# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.
# Example:
# If the above tuples are given as input to the program then the output of the program should be 2.

def input_tuples_list(number):
    list_of_tuples = []
    for i in range(1, number + 1):
        list_of_tuples.append(tuple(input().split()))
    return list_of_tuples

def point_move(arg):
    x_axis = 0
    y_axis = 0
    if arg[0] == "LEFT":
        x_axis -= arg[1]
    elif arg[0] == "RIGHT":
        x_axis += arg[1]
    elif arg[0] == "UP":
        y_axis += arg[1]
    elif arg[0] == "DOWN":
        y_axis -= arg[1]
    return x_axis, y_axis

def end_point_coordinates(arg):
    x, y = 0
    for i in arg:
        x_move, y_move = point_move(arg[i])
        x += x_move
        y += y_move
    return x, y

def distance(arg1, arg2):
    return int((arg1 ** 2 + arg2 ** 2) ** 0.5)

print(distance(end_point_coordinates(input_tuples_list(int(input())))))