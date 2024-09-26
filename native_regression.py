from matrix import *
import sys
import matplotlib.pyplot as plt
path = sys.argv[1]
x,y =transpose(loadtxt(path))
Xp = powers(x,0,1)
Yp = powers(y,1,1)
Xpt = transpose(Xp)
[[b], [m]]=matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))
y2=[]
for temperature in x:
    y2.append((b + m * temperature))
plt.plot(x,y,'ro')
plt.plot(x,y2)
plt.show()
