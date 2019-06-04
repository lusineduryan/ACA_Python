# https://en.wikipedia.org/wiki/LU_decomposition
# https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy

# def scal(arg1, arg2):
#     assert len(arg1) == len(arg2)
#     return sum(map(lambda i, j: i * j, arg1, arg2))
#
# def mat_prod(arg1, arg2):
#     assert len(arg1[0]) == len(arg2[0])
#     return list(map(lambda x, y: list(map(scal, x, y)), list(map(lambda x: [x] * len(arg2), arg1)), [arg2] * len(arg2)))
#
# def pivot_mat(arg):
#     identity_mat = []
#     for i in range(len(arg)):
#         for j in range(len(arg)):
#             identity_mat.append(arg[i,j])
#
#     for i in range(len(arg)):

def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    # Create an identity matrix, with floating point values
    id_mat = [[float(i ==j) for i in range(m)] for j in range(m)]
    print(id_mat)

    # Rearrange the identity matrix such that the largest element of
    # each column of M is placed on the diagonal of of M
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            # Swap the rows
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat

A = [[15, 3, -16, 2], [3, -84, 1, -100], [14, 1, 4, -1], [2, 63, -1, -6]]
print(pivot_matrix(A))


