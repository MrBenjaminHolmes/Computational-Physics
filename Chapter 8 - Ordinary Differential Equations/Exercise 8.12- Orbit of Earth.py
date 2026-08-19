import numpy as np
import matplotlib.pyplot as plt

G = 6.6738e-11          
M = 1.9891e30          
m = 5.9722e24           
h = 3600.0              

years = 1
N = int(years * 365.25 * 24)

r = np.array([1.4710e11, 0.0])
v = np.array([0.0, 3.0287e4])
t = np.arange(N + 1) * h

rs = np.zeros((N + 1, 2))
vs = np.zeros((N + 1, 2))
rs[0] = r
vs[0] = v

total =[]
kinetic =[]
potential =[]


def f(r):
    distance = np.linalg.norm(r)
    return -G * M * r / distance**3


v_half = v + 0.5 * h * f(r)

total = []
kinetic = []
potential = []

distance = np.linalg.norm(r)
KE = 0.5 * m * np.dot(v, v)
PE = -G * M * m / distance

kinetic.append(KE)
potential.append(PE)
total.append(KE + PE)

for i in range(N):
        r = r + h * v_half
        k = h * f(r)
        v = v_half + 0.5 * k
        v_half = v_half + k

        rs[i + 1] = r
        vs[i + 1] = v

        # Energies
        distance = np.linalg.norm(r)

        KE = 0.5 * m * np.dot(v, v)
        PE = -G * M * m / distance

        kinetic.append(KE)
        potential.append(PE)
        total.append(KE + PE)

plt.plot(rs[:, 0], rs[:, 1])
plt.plot(0, 0, 'o')
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Orbit of Earth")
plt.axis("equal")
plt.show()

time = np.arange(N + 1) * h / (365.25 * 24 * 3600)

# Part (b)
plt.figure()
plt.plot(time, kinetic, label="Kinetic")
plt.plot(time, potential, label="Potential")
plt.plot(time, total, label="Total")
plt.xlabel("Time (years)")
plt.ylabel("Energy (J)")
plt.legend()
plt.show()

plt.figure()
plt.plot(time, total)
plt.xlabel("Time (years)")
plt.ylabel("Total energy (J)")
plt.title("Total Energy")
plt.show()