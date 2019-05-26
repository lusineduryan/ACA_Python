def scal(arg1, arg2):
    assert len(arg1) == len(arg2)
    return sum(map(lambda i, j: i * j, arg1, arg2))

#print(scal([1,0,1,2,], [2,4,5,6]))

def mat(arg1, arg2):
    assert len(arg1[0]) == len(arg2[0])
    res = []
    for i in arg1:
        line = []
        for j in arg2:
            line.append(scal(i, j))
        res.append(line)
    return res

print(mat([[1,1],[2,2]], [[1,0], [0,1]]))
