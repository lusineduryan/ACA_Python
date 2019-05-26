#from .Classwork_2_scalarProduct import scal

def scal(arg1, arg2):
    assert len(arg1) == len(arg2)
    return sum(map(lambda i, j: i * j, arg1, arg2))

def trans(arg):
    res = []
    for i in range(len(arg[0])):
        line = []
        for j in arg:
            line.append(j[i])
        res.append(line)
    return res

print(*trans([[1,1,1], [2,2,2]]), sep = '\n')

a = [[1,1],[2,2]]
b = [[3,4],[3,4]]

def mat_prod(arg1, arg2):
    tr = trans(arg2)
    assert len(arg1[0]) == len(arg2[0])
    res = []
    for i in arg1:
        line = []
        for j in tr:
            line.append(scal(i, j))
        res.append(line)
    return res

print(mat_prod(a,b))