def isPowerOfTwo(arg):
    while arg > 1:
        if arg % 2 != 0:
            return False
        arg = arg // 2

    return True

def min_num(arg1, arg2):
    if arg1 == arg2:
        return 1
    else:
        res = min(arg1, arg2)
        for i in range(2, arg1 * arg2, 2):
            if arg1 % i == 0 and arg2 % i == 0:
                if isPowerOfTwo(i):
                    res = i
        return (arg1 * arg2) // (res ** 2)

side1 = 4
side2 = 6
print(min_num(side1, side2))

