from numpy import *
import sys
import matplotlib.pyplot as plt
def powers(input_list, lower_limit, upper_limit):
    return array([[i**j for j in range(lower_limit, upper_limit+1)] for i in input_list])

path = sys.argv[1]
n = sys.argv[2]
x,y=transpose(loadtxt(path))
Xp= powers(x,0,n)
Yp= powers(y,1,1)
Xpt = transpose(Xp)
a=matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a=a[:,0]
print(b)
print(m)
y2=[]
for temperature in x:
    y2.append((b + m * temperature))
plt.plot(x,y,'ro')
plt.plot(x,y2)
plt.show()