from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(input_list, lower_limit, upper_limit):
    return array([[i**j for j in range(lower_limit, upper_limit+1)] for i in input_list])

def poly(a, x):
    return sum([c*x**i for i, c in enumerate(a)])

path, n = sys.argv[1], int(sys.argv[2])
x, y = transpose(loadtxt(path))
Xp = powers(x, 0, n)
Yp = powers(y, 1, 1)
Xpt = transpose(Xp)
a = matmul(linalg.inv(matmul(Xpt,Xp)), matmul(Xpt,Yp))
a = a[:,0]

y2 = []
x2 = linspace(min(x), max(x), 1000)
for val in x2:
    y2.append(poly(a, val))

plt.plot(x, y, 'ro')
plt.plot(x2, y2)
plt.show()
