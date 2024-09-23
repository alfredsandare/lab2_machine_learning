from numpy import *
import sys
import matplotlib.pyplot as plt
def powers(input_list, lower_limit, upper_limit):
    return array([[i**j for j in range(lower_limit, upper_limit+1)] for i in input_list])

path = sys.argv[1]
n = int(sys.argv[2])
x,y=transpose(loadtxt(path))
Xp= powers(x,0,n)
Yp= powers(y,1,1)
Xpt = transpose(Xp)
a=matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a=a[:,0]
print(a)
def poly(a,x):
    output=0
    for i, val in enumerate(a):
        output+=val*x**(i)
    return(output)
y2=[]
x2=range(int(max(x))+1)
for val in x2:
    new=poly(a,val)
    print(new,val)
    y2.append(new)

print()
plt.plot(x,y,'ro')
plt.plot(x2,y2)
plt.show()