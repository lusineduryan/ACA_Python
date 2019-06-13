def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)

some_list = []

def impure_function(arg):
    return some_list.append(arg)