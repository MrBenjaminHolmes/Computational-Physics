from scipy.integrate import fixed_quad
import scipy.constants as consts
import numpy as np
import matplotlib.pyplot as plt

m = 1

def V(x):
    return x**4

def integrand(x, a):
    return 1 / np.sqrt(V(a) - V(x))

def T(a):
    s, error = fixed_quad(integrand, 0, a, args=(a,))
    return np.sqrt(8*m) * s

ampls = np.linspace(0.1,2,1000)
Tls =[]

for a in ampls:
    Tls.append(T(a))

plt.plot(ampls,Tls)
plt.xlabel("Amplitude (m)")
plt.ylabel("Period (s)")
plt.title("Anharmonic Ocsillator")
plt.show()