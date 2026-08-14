import numpy as np 
import matplotlib.pyplot as plt
import scipy.constants as sciconst
from matplotlib.animation import FuncAnimation
g = sciconst.g
l=0.1
C=2
alpha = 9.6
a=0 
b=100
N=10000
h= (b-a)/N
tpoints = np.linspace(a, b, N+1)
thetapoints = []
omegapoints = []


def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = (-(g/l)*np.sin(theta))+(C*np.cos(theta)*np.sin(alpha*t))
    return np.array([ftheta,fomega],float)

rVec = np.array([np.deg2rad(0), 0], dtype=float)
for t in tpoints:
    thetapoints.append(rVec[0])
    omegapoints.append(rVec[1])
    k1=h*f(rVec,t)
    k2= h*f(rVec+0.5*k1,t+0.5*h)
    k3 = h*f(rVec+0.5*k2,t+0.5*h)
    k4 = h*f(rVec+k3,t+h)
    rVec += (k1+2*k2+2*k3+k4)/6 

plt.plot(tpoints,thetapoints)
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (Rad)")
plt.show()
fig, ax = plt.subplots()


ax.set_xlim(-l * 1.2, l * 1.2)
ax.set_ylim(-l * 1.2, l * 1.2)
ax.set_aspect('equal')

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Simple Pendulum")

rod, = ax.plot([], [], 'o-', lw=3)
bob, = ax.plot([], [], 'o', markersize=15)

def update(frame):
    theta = thetapoints[frame]
    x = l * np.sin(theta)
    y = -l * np.cos(theta)
    rod.set_data([x,0],[y,0])
    bob.set_data([x], [y])
    
    return (bob,rod)

animation = FuncAnimation(
    fig,
    update,
    frames=len(thetapoints),
    interval=1,
    blit=True
)

plt.show()