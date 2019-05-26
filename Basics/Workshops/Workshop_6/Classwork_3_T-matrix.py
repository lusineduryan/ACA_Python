def trans(arg):
    res = []
    for i in range(len(arg[0])):
        line = []
        for j in arg:
            line.append(j[i])
        res.append(line)
    return res

print(trans([[1,1,1], [2,2,2]]))