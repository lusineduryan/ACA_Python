def deter(arg):
    assert len(arg) == len(arg[0])
    if len(arg) == 2:
        return arg[0][0] * arg[1][1] - arg[0][1] * arg[1][0]
    else:
        d = 0
        minor = []
        for i in range(len(arg)):
            minor_row = []
            for j in range(len(arg[i])):
                if j != i and j != 0:
                    minor_row.append(arg[i][j])
            minor.append(minor_row)
            d += (-1) ** i * i * deter(minor)
        return d

A = [[0,1,2], [2,3,4], [3,4,6]]
B = [[1,2],[3,4]]
print(deter(B))
print(deter(A))
