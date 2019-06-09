def mult(arg):
    res = arg
    l1 = len(arg)
    for i in range(len(arg)):
        l = len(arg)
        if arg[i] == '*':
            temp = int(arg[i - 1]) * int(arg[i + 1])
            if i == len(arg) - 1:
                arg = arg[:i - 1] + str(temp)
                res = mult(arg)
            elif i == 1:
                arg = str(temp) + arg[i + 2:]
                res = mult(arg)
            else:
                arg = arg[:i - 1] + str(temp) + arg[i + 2:]
                res = mult(arg)
            print(arg)
        else:
            res = mult(arg)
    return res

a = '3+2*3+1'
print(mult(a))
#
# def calculator(arg):
#     arg = mult(arg)
#     res = 0
#     for i in range(len(arg)):
#         if arg[i] == '+':
#             res += int(arg[i-1]) + int(arg[i+1])
#         elif arg[i] == '-':
#             res += int(arg[i-1]) - int(arg[i+1])
#     return res
#
# def scope_calc(arg):
#     for i in range(len(arg)):
#         if arg[i] == '(':
#             temp = arg[i + 1:]
#             for j in range(i + 1, len(arg)):
#                 if arg[j] != '(':
#                     end = temp.find(')')
#                     res = calculator(arg[i + 1: end])
#                 else:
#                     res = scope_calc(arg[j:])

# print(scope_calc(input()))