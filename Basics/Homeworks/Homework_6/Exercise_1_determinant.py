def rec_deter(arg):
    for i in arg:
        assert len(arg) == len(i)
    if len(arg) == 1:
        return arg[0][0]
    if len(arg) == 2:
        return arg[0][0] * arg[1][1] - arg[0][1] * arg[1][0]
    else:
        d = 0
        for i in range(len(arg)):
            minor = []
            for j in arg[1:]:
                minor.append(j[:i] + j[i+1:])
            d += (-1) ** i * i * rec_deter(minor)
        return d

A = [[0,1,2], [2,3,4], [3,4,6]]
print(rec_deter(A))
