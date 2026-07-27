from scipy.integrate import fixed_quad
import scipy.constants as consts
import numpy as np
import matplotlib.pyplot as plt
thetaD = 428
p  = 6.022e28
N=50
V=1000
cvls = []


def f(x):
    return ((x**4)*np.exp(x))/((np.exp(x) -1)**2)

def Cv(T):
    s ,error = fixed_quad(f,0,thetaD/T,n=N)
    return 9*V*p*consts.Boltzmann*((T)/(thetaD))**3 *s

for T in range(5,501):
    cvls.append(Cv(T))

plt.plot(cvls)
plt.xlabel("Temperature (K)")
plt.ylabel("Cv(T)")
plt.title("Specific Heat Capacity of 1000 $\mathregular{m^{3}}$ Aluminium")
plt.grid(True)
plt.show()