# https://en.wikipedia.org/wiki/LU_decomposition
# https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy

def scal(arg1, arg2):
    assert len(arg1) == len(arg2)
    return sum(map(lambda i, j: i * j, arg1, arg2))

def mat_prod(arg1, arg2):
    assert len(arg1[0]) == len(arg2[0])
    return list(map(lambda x, y: list(map(scal, x, y)), list(map(lambda x: [x] * len(arg2), arg1)), [arg2] * len(arg2)))

def identity_mat(arg):
    iden_mat = [[0] * len(arg) for i in range(len(arg))]
    print(iden_mat)
    for i in range(len(iden_mat)):
        iden_mat[i][i] = 1
    return iden_mat

def lu_decomposition(arg):
    P = identity_mat(arg)
    PA = mat_prod(P, arg)
    L = [[0] * len(arg) for i in range(len(arg))]
    U = [[0] * len(arg) for i in range(len(arg))]
    for j in range(len(arg)):
        L[j][j] = 1
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1
        for i in range(j, len(arg)):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

    return (L, U)

def det(arg1):
    l, u = lu_decomposition(arg1)
    p1, p2 = 1, 1
    for i in range(len(l)):
       p1 *= l[i][i]
    for i in range(len(u)):
        p2 *= u[i][i]
    return p1 * p2



A = [[15, 3, -16, 2], [3, -84, 1, -100], [14, 1, 400, -1], [2, 63, -1, -6]]
print(det(A))

import numpy as np

print(np.linalg.det(A))


