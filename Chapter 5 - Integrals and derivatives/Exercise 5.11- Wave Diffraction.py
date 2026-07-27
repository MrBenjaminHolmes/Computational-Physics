from scipy.integrate import fixed_quad
import scipy.constants as consts
import numpy as np
import matplotlib.pyplot as plt

wavelen = 1
z=3

def C(p):
    integrandc = lambda t: np.cos(0.5*np.pi*t**2)
    s, error = fixed_quad(integrandc, 0, p, n=50)
    return s

def S(p):
    integrands = lambda t: np.sin(0.5*np.pi*t**2)
    s, error = fixed_quad(integrands, 0, p, n=50)
    return s

x = np.linspace(-5,5,1000)
u = x*np.sqrt((2)/(wavelen*z))

Cvalues = np.array([C(p) for p in u])
Svalues = np.array([S(p) for p in u])

Iratio = ((2 * Cvalues +1)**2 + (2 * Svalues+1)**2) / 8

plt.plot(x, Iratio)
plt.xlabel("x")
plt.ylabel("Intensity ratio")
plt.show()