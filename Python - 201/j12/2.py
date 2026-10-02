import numpy as np

a = np.array([
    [1 , 2 , 3],
    [4 , 5 , 6],
]
)
b = np.zeros(5)
c = np.ones(3)
d = np.arange(1 , 11)


print(a)
print(b)
print(c)
print(d)


print(a[0 , 1])

print(np.mean(a))

s = np.concatenate((b , c))
print(s)

t = d.reshape(3 , 3)
print(t)