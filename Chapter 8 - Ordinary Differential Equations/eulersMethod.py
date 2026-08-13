import numpy as np 
import matplotlib.pyplot as plt

def f(x,t):
    return -x**3 + np.sin(t)

a=0
b=10
N=1000
h=(b-a)/N
x=0

tpoints = np.arange(a,b,h)
xpoints = []
for t in tpoints:
    xpoints.append(x)
    x+=h*f(x,t)

plt.plot(tpoints,xpoints)
plt.show()