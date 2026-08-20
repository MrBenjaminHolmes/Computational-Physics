import numpy as np
import matplotlib.pyplot as plt

size = 100
a=1/size
e0=1
targetError = 10e-6
chargeDensityGrid = np.zeros((size, size))
electricPotential = np.zeros((size,size))
def chargeDensity(x, y):

    # + square
    if 0.2 <= x <= 0.4 and 0.2 <= y <= 0.4:
        return 10000

    # - square
    elif 0.6 <= x <= 0.8 and 0.6 <= y <= 0.8:
        return -10000

    return 0

for i in range(size):
    for j in range(size):
        x = i / size
        y = j / size

        chargeDensityGrid[i, j] = chargeDensity(x, y)

plt.imshow(
    chargeDensityGrid,
    origin="lower",
    extent=[0, 1, 0, 1]
)

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.colorbar(label="Charge density")
plt.show()
electricPotentialPrime = np.empty((size,size))
delta = 1.00
while delta > targetError:

    for i in range(1, size - 1):
        for j in range(1, size - 1):

            electricPotentialPrime[i, j] = (
                electricPotential[i + 1, j]
                + electricPotential[i - 1, j]
                + electricPotential[i, j + 1]
                + electricPotential[i, j - 1]
            ) / 4 + (
                a**2 / (4 * e0)
            ) * chargeDensityGrid[i, j]

    # Boundary conditions
    electricPotentialPrime[0, :] = 0
    electricPotentialPrime[-1, :] = 0
    electricPotentialPrime[:, 0] = 0
    electricPotentialPrime[:, -1] = 0

    delta = np.max(
        np.abs(electricPotentialPrime - electricPotential)
    )
    electricPotential = electricPotentialPrime.copy()

plt.imshow(
    electricPotential,
    origin="lower",
    extent=[0, 1, 0, 1]
)

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.colorbar(label="Electric potential")
plt.show()