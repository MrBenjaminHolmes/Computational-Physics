import numpy as np 
import matplotlib.pyplot as plt

Omega = 1
a=0
b=50
N=10000
h= (b-a)/N


def HarmonicFunc(r,t):
    x = r[0]
    alpha = r[1]
    fx = alpha
    falpha = -(Omega**2)*x
    return np.array([fx,falpha],float)

def AnarmonicFunc(r,t):
    x = r[0]
    alpha = r[1]
    fx = alpha
    falpha = -(Omega**2)*x**3
    return np.array([fx,falpha],float)

def rk4(initx,initdxdt,Omega,f):
    tpoints = np.arange(a,b,h)
    xpoints = []
    alphapoints = []
    rVec = np.array([initx,initdxdt], dtype=float)

    for t in tpoints:
        xpoints.append(rVec[0])
        alphapoints.append(rVec[1])
        k1=h*f(rVec,t)
        k2= h*f(rVec+0.5*k1,t+0.5*h)
        k3 = h*f(rVec+0.5*k2,t+0.5*h)
        k4 = h*f(rVec+k3,t+h)
        rVec += (k1+2*k2+2*k3+k4)/6 

    return tpoints,xpoints,alphapoints

case1 = rk4(1,0,1,HarmonicFunc)
case2 = rk4(2,0,1,HarmonicFunc)
plt.plot(case1[0],case1[1])
plt.plot(case2[0],case2[1])
plt.title("Harmonic Oscillator Amplitude vs Period")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.show()

case3 = rk4(1,0,1,AnarmonicFunc)
case4 = rk4(2,0,1,AnarmonicFunc)
plt.plot(case3[0],case3[1])
plt.plot(case4[0],case4[1])
plt.title("Anharmonic Oscillator Amplitude vs Period")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.show()

plt.plot(case3[1], case3[2])
plt.title("Anharmonic Oscillator Phase Space")
plt.xlabel("Position (m)")
plt.ylabel("Velocity (m/s)")
plt.show()