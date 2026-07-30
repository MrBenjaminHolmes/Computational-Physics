import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants

width = 500
height = 500

potentialGrid = np.zeros((height, width))


particle1 = [-5, 0, 1]
particle2 = [5, 0, -1]

particleLst = [particle1, particle2]


def phi(q, r):
    return q / (4 * np.pi * constants.epsilon_0 * r)


for i in range(width):
    for j in range(height):

        x = (i / (width - 1)) * 100 - 50
        y = (j / (height - 1)) * 100 - 50

        for particle in particleLst:

            r_cm = np.sqrt(
                (particle[0] - x)**2 +
                (particle[1] - y)**2
            )

            if r_cm != 0:

                r = r_cm / 100

                potentialGrid[j, i] += phi(particle[2], r)


plt.imshow(
    potentialGrid,
    origin="lower",
    extent=[-50, 50, -50, 50],
    vmax=5e10,
    vmin=-5e10,
    cmap="jet"
)

plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.colorbar(label="Potential (V)")
plt.show()

dVdy, dVdx = np.gradient(
    potentialGrid,
    1 / (height - 1),
    1 / (width - 1)
)

Ex = -dVdx
Ey = -dVdy

# Magnitude of electric field
E = np.sqrt(Ex**2 + Ey**2)

# Normalize field vectors
Ex_norm = Ex / (E + 1e-30)
Ey_norm = Ey / (E + 1e-30)

step = 15

x = np.linspace(-50, 50, width)
y = np.linspace(-50, 50, height)

X, Y = np.meshgrid(x, y)

plt.figure(figsize=(8, 8))

# Potential underneath
plt.imshow(
    potentialGrid,
    origin="lower",
    extent=[-50, 50, -50, 50],
    vmax=5e10,
    vmin=-5e10,
    cmap="jet"
)

# Electric field direction
plt.quiver(
    X[::step, ::step],
    Y[::step, ::step],
    Ex_norm[::step, ::step],
    Ey_norm[::step, ::step],
    color="white",
    pivot="mid",
    scale=25
)

plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.title("Electric Field")
plt.axis("equal")
plt.show()