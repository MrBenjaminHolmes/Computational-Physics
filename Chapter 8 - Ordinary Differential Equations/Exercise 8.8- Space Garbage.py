import numpy as np
import matplotlib.pyplot as plt


#---Constants---#
G=1
M=10
L=2

a=0
b=10
N=10000
h= (b-a)/N

def OrbitFunc(r,t):
    x = r[0]
    alpha = r[1]
    y = r[2]
    beta = r[3]

    r = np.sqrt(x**2 + y**2)

    fx = alpha
    falpha = -(G*M)*((x)/(r**2 * np.sqrt(r**2 + (L**2)/(4))))
    fy = beta
    fbeta = -(G*M)*((y)/(r**2 * np.sqrt(r**2 + (L**2)/(4))))
    return np.array([fx,falpha,fy,fbeta],float)

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

orbit = rk4([1, 0, 0, 1], OrbitFunc)
plt.plot(orbit[1],orbit[3])
plt.xlabel("x")
plt.title("Ball Bearing Orbiting Metal Rod in Empty Space")
plt.ylabel("y")
plt.axis("equal")
plt.show()