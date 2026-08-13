import numpy as np
import matplotlib.pyplot as plt


alpha = 1
beta =  gamma = 0.5
sigma = 2
x = y = 2

a=0
b=30
N=1000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
ypoints = []


def f(r,t):
    x=r[0]
    y=r[1]
    fx = (alpha*x)-(beta*x*y)
    fy = (gamma*x*y) - (sigma*y)
    return np.array([fx,fy],float)


r = np.array([2.0,2.0])
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1=h*f(r,t)
    k2= h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r+= (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints,xpoints)
plt.plot(tpoints,ypoints)
plt.show()