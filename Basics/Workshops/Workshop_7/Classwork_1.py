import numpy as np

a = list(range(100))
print(np.array(a).shape)
b = np.array(a).reshape(-1,1)
c = np.array(a).reshape(1,-1)
print(b, b.shape)
print(c, c.shape)

a_2 = np.array([[1,2,3], [8,10,15],[8,9,2]])
print(a_2[:, 0])
print(a_2[1])

print(a_2[0,: -1])
print(a_2[:-1, :-1])

print(np.linalg.det(a_2))

print(a_2.mean(axis = 1))
