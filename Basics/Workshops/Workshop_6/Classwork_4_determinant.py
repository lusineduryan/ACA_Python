def deter(arg):
    assert len(arg) == len(arg[0])
    if len(arg) == 2:
        return arg[0][0] * arg[1][1] - arg[0][1] * arg[1][0]
    else:
        det = 0
        for i in arg[0]:
            m = arg.remove(i).remove(arg[1][0]).remove(arg[2][0])
            det += (-1) * (i.inde + 1) * det(m)
            return det

A = [[1,5,-1], [1,2,3], [2,3,4]]

print(deter(A))