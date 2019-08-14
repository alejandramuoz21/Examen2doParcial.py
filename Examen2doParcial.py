from Lineal import *
from numpy import *
a = array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]], float)
b = array([[11], [-16], [17]], float)
c = concatenate([a, b], axis=1)
print(c)
print(gaussjordan1(a,b))


from Lagrange import *
x = [-2, 1, 4, -1, 3, -4]
y = [-1, 2, 59, 4, 24, -53]
p = lagrange(x, y)
print(p)
r = lagrange(x, y, 4.25)
print(r)
r = lagrange(x, y, [3.15, 3.74, 4.25])
print(r)


