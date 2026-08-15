import numpy as np 
import matplotlib.pyplot as plt

#---Constants---#
R=0.08
theta = 30
v=100
p=1.22
C=0.47
g= 9.81

a=0
b=8
N=10000
h= (b-a)/N

def TrajectoryFunc(r,t,m):
    x = r[0]
    alpha = r[1]
    y = r[2]
    beta = r[3]
    fx = alpha
    falpha = -((np.pi*(R**2)*p*C)/(2*m) * alpha * np.sqrt(alpha**2 + beta**2))
    fy = beta
    fbeta = -g-((np.pi*(R**2)*p*C)/(2*m) * beta * np.sqrt(alpha**2 + beta**2))
    return np.array([fx,falpha,fy,fbeta],float)

def rk4(init,f):
    tpoints = np.arange(a,b,h)
    xpoints = []
    alphapoints = []
    ypoints = []
    betapoints = []
    rVec = np.array(init[:-1], dtype=float)

    for t in tpoints:
        xpoints.append(rVec[0])
        alphapoints.append(rVec[1])
        ypoints.append(rVec[2])
        betapoints.append(rVec[3])
        k1=h*f(rVec,t,init[-1])
        k2= h*f(rVec+0.5*k1,t+0.5*h,init[-1])
        k3 = h*f(rVec+0.5*k2,t+0.5*h,init[-1])
        k4 = h*f(rVec+k3,t+h,init[-1])
        rVec += (k1+2*k2+2*k3+k4)/6 

    return tpoints,xpoints,alphapoints, ypoints, betapoints

Trajectory = rk4(
    [
        0,
        v*np.cos(np.deg2rad(theta)),
        0,
        v*np.sin(np.deg2rad(theta)),
        1 # mass
    ],
    TrajectoryFunc
)

tpoints, xpoints, alphapoints, ypoints, betapoints = Trajectory

plt.plot(xpoints, ypoints,label="M=1")

Trajectory = rk4(
    [
        0,
        v*np.cos(np.deg2rad(theta)),
        0,
        v*np.sin(np.deg2rad(theta)),
        2 # mass
    ],
    TrajectoryFunc
)

tpoints, xpoints, alphapoints, ypoints, betapoints = Trajectory

plt.plot(xpoints, ypoints,label="M=2")

Trajectory = rk4(
    [
        0,
        v*np.cos(np.deg2rad(theta)),
        0,
        v*np.sin(np.deg2rad(theta)),
        4 # mass
    ],
    TrajectoryFunc
)

tpoints, xpoints, alphapoints, ypoints, betapoints = Trajectory

plt.plot(xpoints, ypoints,label="M=4")

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.show()