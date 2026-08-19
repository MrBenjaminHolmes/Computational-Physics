import numpy as np 
import matplotlib.pyplot as plt
from scipy.constants import G

Mass = 1.9884099e+30
a = 0
b = 4.8e9     
h = 10000
N = int((b-a)/h)
def OrbitFODE(r, t):
    x = r[0]
    alpha = r[1]
    y = r[2]
    beta = r[3]

    d = np.sqrt(x**2 + y**2)

    fx = alpha
    falpha = -G * Mass * (x / d**3)
    fy = beta
    fbeta = -G * Mass * (y / d**3)

    return np.array([fx, falpha, fy, fbeta], float)

def rk4(init,f):
    tpoints = np.arange(a,b,h)
    xpoints = []
    alphapoints = []
    ypoints = []
    betapoints = []
    rVec = np.array(init, dtype=float)

    for t in tpoints:
        xpoints.append(rVec[0])
        alphapoints.append(rVec[1])
        ypoints.append(rVec[2])
        betapoints.append(rVec[3])
        k1=h*f(rVec,t)
        k2= h*f(rVec+0.5*k1,t+0.5*h)
        k3 = h*f(rVec+0.5*k2,t+0.5*h)
        k4 = h*f(rVec+k3,t+h)
        rVec += (k1+2*k2+2*k3+k4)/6 

    return tpoints,xpoints,alphapoints, ypoints, betapoints

orbit = rk4([4e12, 0, 0, 500], OrbitFODE)
plt.plot(orbit[1],orbit[3])
plt.xlabel("x")
plt.title("Cometary Orbit around the Sun")
plt.ylabel("y")
plt.show()