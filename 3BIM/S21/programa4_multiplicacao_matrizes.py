import numpy as np

v1 = np.array([[1, 2], [3, 4]])
v2 = np.array([[1, 2], [3, 4]])

print("v1 =\n", v1)
print("v2 =\n", v2)

resultado1 = v1 * v2
print("v1*v2 = \n", resultado1)

resultado2 = np.dot(v1, v2)
print("\nnp.dot(v1,v2) = \n", resultado2)
