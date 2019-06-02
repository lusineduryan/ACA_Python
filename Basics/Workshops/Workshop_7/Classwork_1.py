import numpy as np

a = list(range(100))
print(np.array(a).shape)
b = np.array(a).reshape(10,10)
print(b, b.shape)

a_2 = np.array([[1,2,3], [8,10,15],[8,9,2]])
print(a_2[:, 0])
print(a_2[1])

print(a_2[0,: -1])
print(a_2[:-1, :-1])
