# https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-determinants-and-inverses-of-large-matrices/v/finding-the-determinant-of-a-3x3-matrix-method-1

def fast_deter(arg):
    res = 0
    N1 = arg
    for i in range(len(arg)):
        if i > 0:
            N1 = N1[1:]
            N1.append(arg[i-1])
        N2 = N1[::-1]
        prod1, prod2 = 1, 1
        for j in range(len(N1)):
            prod1 *= N1[j][j]
        for k in range(len(N2)):
            prod2 *= N2[k][k]
        temp_res = prod1 - prod2
        res += temp_res
    return res

A = [[0,2,3], [1,3,4], [2,4,6]]
print(fast_deter(A))

