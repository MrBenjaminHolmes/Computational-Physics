from scipy.integrate import dblquad
import scipy.constants as constant
import numpy as np
import matplotlib.pyplot as plt

L = 10
sigma = 10000/100
z_values = np.linspace(0.0001, 10, 1000)
Fz_values = []

for z in z_values:

    # Integrand
    fz = lambda y, x: 1 / (x**2 + y**2 + z**2)**(3/2)

    s, error = dblquad(
        fz,
        -L/2, L/2,
        lambda x: -L/2,
        lambda x: L/2
    )
    Fz = constant.G * sigma * z * s

    Fz_values.append(Fz)

plt.plot(z_values, Fz_values)

plt.xlabel("Distance z (m)")
plt.ylabel("$F_z$ (N)")
plt.title("Gravitational force vs distance from square plate")
plt.grid()
plt.show()