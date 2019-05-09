# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console.
# The sort criteria is:1: Sort based on name;2: Then sort based on age;3: Then sort by score.The priority is that name > age > score.If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')].

def input_tuples_list(number):
    list_of_tuples = []
    for i in range(1, number + 1):
        list_of_tuples.append(tuple(input().split(',')))
    return list_of_tuples

def tuple_comparison(arg1, arg2):
    if arg1[0] > arg2[0]:
        return True
    elif arg1[0] == arg2[0]:
        if int(arg1[1]) > int(arg2[1]):
            return True
        elif int(arg1[1] == int(arg2[1])):
            if int(arg1[2]) > int(arg2[2]):
                return True

def sorting_tuples(arg):
    for i in range(len(arg)):
        for j in range(len(arg) - i - 1):
            if tuple_comparison(arg[j], arg[j + 1]):
                arg[j], arg[j + 1] = arg[j + 1], arg[j]
    return arg

print(sorting_tuples(input_tuples_list(int(input()))))

