from numpy import array, arange, trapz
import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 9.1094e-31
hbar = 1.0546e-34
e = 1.6022e-19

V0 = 50 * e
a = 1.0e-11

# Numerical grid
N = 10000
xmax = 10 * a
h = xmax / N

x_positive = arange(0, xmax, h)


# Potential
def V(x):
    return V0 * (x**2) / (a**2)


# First-order equations
def f(r, x, E):
    psi = r[0]
    phi = r[1]

    fpsi = phi
    fphi = (2*m/hbar**2) * (V(x) - E) * psi

    return array([fpsi, fphi], float)


# Solve and store the wavefunction
def solve_wavefunction(E, parity):

    if parity == "even":
        psi = 1.0
        phi = 0.0
    else:
        psi = 0.0
        phi = 1.0

    r = array([psi, phi], float)

    psi_values = [psi]

    for x in x_positive[:-1]:

        k1 = h * f(r, x, E)
        k2 = h * f(r + 0.5*k1, x + 0.5*h, E)
        k3 = h * f(r + 0.5*k2, x + 0.5*h, E)
        k4 = h * f(r + k3, x + h, E)

        r += (k1 + 2*k2 + 2*k3 + k4) / 6

        psi_values.append(r[0])

    return array(psi_values)

def normalize_wavefunction(psi):

    # Only integrate out to 5a
    cutoff = x_positive <= 5*a

    x_norm = x_positive[cutoff]
    psi_norm = psi[cutoff]

    # Integral from 0 to 5a
    integral_half = trapz(psi_norm**2, x_norm)

    # Symmetry: integral from -infinity to infinity
    # is twice the integral from 0 to infinity
    integral_total = 2 * integral_half

    # Normalization constant
    normalization = np.sqrt(integral_total)

    return psi / normalization


E0 = 138.0239720296056 * e
E1 = 414.07191608884193 * e
E2 = 690.1198601480782 * e


psi0_positive = solve_wavefunction(E0, "even")
psi1_positive = solve_wavefunction(E1, "odd")
psi2_positive = solve_wavefunction(E2, "even")


psi0_positive = normalize_wavefunction(psi0_positive)
psi1_positive = normalize_wavefunction(psi1_positive)
psi2_positive = normalize_wavefunction(psi2_positive)

cutoff = x_positive <= 5*a

xp = x_positive[cutoff]

psi0p = psi0_positive[cutoff]
psi1p = psi1_positive[cutoff]
psi2p = psi2_positive[cutoff]


x0 = np.concatenate((-xp[:0:-1], xp))
psi0 = np.concatenate((psi0p[:0:-1], psi0p))
psi2 = np.concatenate((psi2p[:0:-1], psi2p))


x1 = np.concatenate((-xp[:0:-1], xp))
psi1 = np.concatenate((-psi1p[:0:-1], psi1p))


plt.figure(figsize=(9, 6))

plt.plot(x0/a, psi0, label="Ground state")
plt.plot(x1/a, psi1, label="First excited state")
plt.plot(x0/a, psi2, label="Second excited state")

plt.xlabel("x/a")
plt.ylabel(r"$\psi(x)$")
plt.title("Normalized Harmonic Oscillator Wavefunctions")

plt.axhline(0, linewidth=0.8)
plt.legend()
plt.grid(True)

plt.xlim(-5, 5)

plt.show()