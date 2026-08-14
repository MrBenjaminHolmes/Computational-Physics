import numpy as np
import matplotlib.pyplot as plt

sigma = 10
r=28
b=8/3

a=0
bRk=50
n=100000
h=(bRk-a)/n

tpoints = np.arange(a,bRk,h)
xpoints = []
ypoints = []
zpoints = []

def f(rInput, t):
    x = rInput[0]
    y = rInput[1]
    z = rInput[2]

    fx = sigma * (y - x)
    fy = r * x - y - x * z
    fz = x * y - b * z

    return np.array([fx, fy, fz], float)

rVec = np.array([0, 1, 0], dtype=float)
for t in tpoints:
    xpoints.append(rVec[0])
    ypoints.append(rVec[1])
    zpoints.append(rVec[2])
    k1=h*f(rVec,t)
    k2= h*f(rVec+0.5*k1,t+0.5*h)
    k3 = h*f(rVec+0.5*k2,t+0.5*h)
    k4 = h*f(rVec+k3,t+h)
    rVec += (k1+2*k2+2*k3+k4)/6



fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot(xpoints, ypoints, zpoints, linewidth=0.6)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Lorenz Attractor")

plt.tight_layout()
plt.show()