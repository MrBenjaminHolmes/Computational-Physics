import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.6738e-11
M = 1.9891e30

# Time interval
a = 0.0
b = 250*3.154e7             

H = 7 * 24 * 60 * 60

delta = 1000.0


# Equations of motion


def f(r):

    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]

    distance = np.sqrt(x**2 + y**2)

    ax = -G * M * x / distance**3
    ay = -G * M * y / distance**3

    return np.array([
        vx,
        ax,
        vy,
        ay
    ])

def modified_midpoint(r, H, n):

    h = H / n

    r1 = r + h * f(r)
    r2 = r + 2 * h * f(r1)

    for i in range(n - 2):

        r1, r2 = r2, r1 + 2 * h * f(r2)

    return 0.5 * (r1 + r2 + h * f(r2))

def bulirsch_stoer(r, H, delta):

    # First modified midpoint calculation
    n = 2

    R = np.empty((1, 4), float)

    R[0] = modified_midpoint(r, H, n)

    error = np.inf

    while error > delta:

        # Increase number of modified-midpoint steps
        n += 2

        # New modified midpoint estimate
        midpoint = modified_midpoint(r, H, n)

        # Previous extrapolation table
        R_old = R.copy()

        # Number of rows in new table
        rows = n // 2

        R = np.empty((rows, 4), float)

        R[0] = midpoint

        # Richardson extrapolation
        for m in range(1, rows):

            factor = (n / (n - 2))**(2 * m)

            R[m] = (
                R[m - 1]
                + (R[m - 1] - R_old[m - 1])
                / (factor - 1)
            )

        # Estimate error using highest two estimates
        error = np.max(
            np.abs(R[rows - 1] - R_old[rows - 2])
        )

    # Highest-order estimate
    return R[rows - 1]

#EARTH----------------------------------
r = np.array([
    1.4710e11,
    0.0,
    0.0,
    3.0287e4
], float)

t = a

xpoints = []
ypoints = []

while t < b:

    xpoints.append(r[0])
    ypoints.append(r[2])

    r = bulirsch_stoer(r, H, delta)

    t += H

plt.plot(xpoints, ypoints , label = "Earth")


#PLUTO----------------------------------
r = np.array([
    4.4368e12,
    0.0,
    0.0,
    6.1218e3
], float)

t = a

xpoints = []
ypoints = []

while t < b:

    xpoints.append(r[0])
    ypoints.append(r[2])

    r = bulirsch_stoer(r, H, delta)

    t += H

plt.plot(xpoints, ypoints , label = "Pluto")



plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Orbit using the Bulirsch-Stoer Method")
plt.axis("equal")
plt.legend()
plt.grid()
plt.show()