import numpy as np

a1 = np.array([1 , 2 , 3])
a2 = np.zeros(5)
a3 = np.ones(4)
a4 = np.arange(1 , 10)
a5 = np.eye(3)

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

print(np.sum(a1))

a6 = np.concatenate((a1 , a2))

print(a6)

print(np.argmin(a4))
print(np.argmax(a4))

a7 = a4.reshape(3 , 3)

print(a7)

print(np.sort(a5))

print(a1[2])

print(a1.ndim)
print(a1.shape)
print(a1.size)