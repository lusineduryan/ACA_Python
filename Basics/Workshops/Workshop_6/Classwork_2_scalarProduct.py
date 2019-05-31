def scal(arg1, arg2):
    assert len(arg1) == len(arg2)
    return sum(map(lambda i, j: i * j, arg1, arg2))

print(scal([1,0,1,2,], [2,4,5,6]))

def mat(arg1, arg2):
    assert len(arg1[0]) == len(arg2[0])
    res = []
    for i in arg1:
        line = []
        for j in arg2:
            line.append(scal(i, j))
        res.append(line)
    return res

print(*mat([[1,1],[2,2]], [[1,0], [0,1]]), sep = '\n')

def mat_2(arg1, arg2):
    assert len(arg1[0]) == len(arg2[0])
    res = []
    for i in range(len(arg1)):
        temp_res = list(map(scal, [arg1[i]] * len(arg2), arg2))
        res.append(temp_res)
    return res

print(*mat_2([[1,1],[2,2]], [[1,0], [0,1]]), sep = '\n')


def mat_prod(arg1, arg2):
    assert len(arg1[0]) == len(arg2[0])
    return list(map(lambda x, y: list(map(scal, x, y)), list(map(lambda x: [x] * len(arg2), arg1)), [arg2] * len(arg2)))

print(*mat_prod([[1,1],[2,2],[5,5]], [[3,4],[3,4],[3,4],[3,4]]), sep = '\n')