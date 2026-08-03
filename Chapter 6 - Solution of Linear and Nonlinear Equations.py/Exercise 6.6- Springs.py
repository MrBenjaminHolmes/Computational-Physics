from numpy import zeros,empty
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Constants
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2*k-m*omega*omega

# Set up the initial values of the arrays
A = zeros([N,N],float)
for i in range(N-1):
    A[i,i] = alpha
    A[i,i+1] = -k
    A[i+1,i] = -k
A[0,0] = alpha - k
A[N-1,N-1] = alpha - k

v = zeros(N,float)
v[0] = C

# Perform the Gaussian elimination
for i in range(N-1):

    # Divide row i by its diagonal element
    A[i,i+1] /= A[i,i]
    v[i] /= A[i,i]

    # Now subtract it from the next row down
    A[i+1,i+1] -= A[i+1,i]*A[i,i+1]
    v[i+1] -= A[i+1,i]*v[i]

# Divide the last element of v by the last diagonal element
v[N-1] /= A[N-1,N-1]

# Backsubstitution
x = empty(N,float)
x[N-1] = v[N-1]
for i in range(N-2,-1,-1):
    x[i] = v[i] - A[i,i+1]*x[i+1]

rest = np.arange(N) * 2
y = np.zeros(N)

fig, ax = plt.subplots(figsize=(12,2))

ax.set_xlim(-1, rest[-1] + 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_yticks([])
ax.set_xlabel("Position")

spring, = ax.plot([], [], 'k-')
masses, = ax.plot([], [], 'o', markersize=12)

def update(frame):
    t = frame * 0.05

    displacement = x * np.cos(omega * t)
    xpos = rest + displacement

    spring.set_data(xpos, y)
    masses.set_data(xpos, y)

    return spring, masses

ani = FuncAnimation(
    fig,
    update,
    frames=300,
    interval=20,
    blit=True
)

plt.show()