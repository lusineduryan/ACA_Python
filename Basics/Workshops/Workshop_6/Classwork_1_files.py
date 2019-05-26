import pickle

a = {"Lucy": 25}

with open('test1.txt', 'xb') as fd:
    pickle.dump(a, fd)

with open('test1.txt', 'rb') as fd:
    print(pickle.load(fd))