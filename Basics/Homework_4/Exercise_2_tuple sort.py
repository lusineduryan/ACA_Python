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

# print(sorted(input_tuples_list(int(input()))))

def swap_items(arg1, arg2, arg3):
    temp = arg1[arg2]
    arg1[arg2] = arg1[arg3]
    arg1[arg3] = temp
    return arg1

def sorting_tuples(arg):
    base = arg[0]
    for i in arg:
        if i[0] > base[0]:
            swap_items(arg, arg.index(i), arg.index(base))





