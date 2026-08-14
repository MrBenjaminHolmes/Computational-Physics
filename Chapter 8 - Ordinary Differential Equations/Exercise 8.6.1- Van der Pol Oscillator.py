import numpy as np 
import matplotlib.pyplot as plt


a=0
b=20
N=10000
h= (b-a)/N


def HarmonicFunc(r,t,Omega,U):
    x = r[0]
    alpha = r[1]
    fx = alpha
    falpha = (U*(1-(x**2))*alpha) - ((Omega**2)*x)
    return np.array([fx,falpha],float)


def rk4(initx,initdxdt,Omega,U,f):
    tpoints = np.arange(a,b,h)
    xpoints = []
    alphapoints = []
    rVec = np.array([initx,initdxdt], dtype=float)

    for t in tpoints:
        xpoints.append(rVec[0])
        alphapoints.append(rVec[1])
        k1=h*f(rVec,t,Omega,U)
        k2= h*f(rVec+0.5*k1,t+0.5*h,Omega,U)
        k3 = h*f(rVec+0.5*k2,t+0.5*h,Omega,U)
        k4 = h*f(rVec+k3,t+h,Omega,U)
        rVec += (k1+2*k2+2*k3+k4)/6 

    return tpoints,xpoints,alphapoints

vanDerPol = rk4(1,0,1,0,HarmonicFunc)
plt.plot(vanDerPol[1], vanDerPol[2],linewidth=0.8)
vanDerPol = rk4(1,0,1,1,HarmonicFunc)
plt.plot(vanDerPol[1], vanDerPol[2],linewidth=0.8)
vanDerPol = rk4(1,0,1,2,HarmonicFunc,)
plt.plot(vanDerPol[1], vanDerPol[2],linewidth=0.8)
vanDerPol = rk4(1,0,1,4,HarmonicFunc)
plt.plot(vanDerPol[1], vanDerPol[2],linewidth=0.8)

plt.title("Van der Pol Oscillator Phase Space")
plt.grid()
plt.axis('equal')
plt.show()