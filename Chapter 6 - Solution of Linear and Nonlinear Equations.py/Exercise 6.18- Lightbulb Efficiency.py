import numpy as np 
import matplotlib.pyplot as plt
import scipy.constants as sciconst
from scipy.integrate import quad

lambda1 = 390e-9
lambda2 = 750e-9
Kb = sciconst.Boltzmann
h  = sciconst.h
c  = sciconst.c
z  = sciconst.golden_ratio

def integral(T):

    def integrand(x):
        return (x**3)/(np.exp(x)-1)
    
    val, _ = quad(integrand, ((h*c)/(lambda2*Kb*T)), ((h*c)/(lambda1*Kb*T)))
    return (15/(np.pi**4))*val

Tvals = np.linspace(300,10000,100000)
efficiency = [integral(T) for T in Tvals]
plt.plot(Tvals,efficiency)
plt.xlabel("Temperature (K)")
plt.ylabel("Efficiency")
plt.grid()
plt.show()

#Golden Ratio Search

x1 = 6000
x4 = 8000

x2 = x4 - (1 / z) * (x4 - x1)
x3 = x1 + (1 / z) * (x4 - x1)

fx1 = integral(x1)
fx2 = integral(x2)
fx3 = integral(x3)
fx4 = integral(x4)

accuracy = 1
while x4-x1 > accuracy:
    if fx2 < fx3:
        x1 = x2
        x2 = x3
        fx2 = fx3

        x3 = x1 + (1 / z) * (x4 - x1)
        fx3 = integral(x3)

    else:
        x4 = x3
        x3 = x2
        fx3 = fx2

        x2 = x4 - (1 / z) * (x4 - x1)
        fx2 = integral(x2)

Tmax = (x2 + x3) / 2
max_efficiency = integral(Tmax)

print("Temperature of maximum efficiency:", Tmax, "K")
print("Maximum efficiency:", max_efficiency)

#Temperature of maximum efficiency: 6928.4637763413775 K
#Maximum efficiency: 0.45169384010084507