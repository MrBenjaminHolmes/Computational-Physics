
import numpy as np
from scipy.integrate import fixed_quad
import matplotlib.pyplot as plt

slit_separation = 20e-6
a = np.pi / slit_separation
wavelength = 500e-9
f = 1
w = 10 * slit_separation
res = 10000
width = 10000
height = 800

diffractionPattern = np.zeros((height, width))

slit1 = 10e-6
slit2 = 20e-6
gap = 60e-6

def q(u):
    slit_1 = (-slit1/2 <= u) & (u <= slit1/2)
    slit_2 = (gap + slit2/2 <= u) & (u <= gap + 3*slit2/2)

    return slit_1 | slit_2

#def q(u):
    #return (np.sin(a * u))**2
    #return (np.sin(a * u))**2 * (np.sin(a/2 * u))**2

def I(x):
    integrand = lambda u: (
        np.sqrt(q(u)) *
        np.exp((1j * 2 * np.pi * x * u) / (wavelength * f))
    )
    s, _ = fixed_quad(integrand, -w/2, w/2, n=100)
    return np.abs(s)**2

xvals = np.linspace(-0.1, 0.1, width)
intensitylst = [I(x) for x in xvals]

diffractionPattern = np.tile(intensitylst, (height, 1))


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))
ax1.imshow(
    diffractionPattern,
    cmap="gray",
    aspect="auto",
    vmax=np.max(diffractionPattern) * 0.2
)
ax1.set_ylabel("Height")
ax1.set_title("Diffraction Pattern")

ax2.plot(xvals, intensitylst, linewidth=2)
ax2.set_xlabel("Position x (mm)")
ax2.set_ylabel("Relative intensity")
ax2.set_title("Intensity Profile")

plt.tight_layout()
plt.show()

