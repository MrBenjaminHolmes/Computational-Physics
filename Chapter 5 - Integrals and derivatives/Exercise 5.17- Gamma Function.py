import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import fixed_quad

def f(a,x):
    return x**(a-1)*np.exp(-x)

xvals = np.linspace(0,5,100)
a2 = [f(2,x) for x in xvals]
a3 = [f(3,x) for x in xvals]
a4 = [f(4,x) for x in xvals]
plt.plot(xvals,a2, label="a=2")
plt.plot(xvals,a3, label="a=3")
plt.plot(xvals,a4, label="a=4")
plt.legend()
plt.show()

def g(a,x):
    return np.exp((a - 1) * np.log(x) - x)

def gamma(a):
    c = a - 1  # From part c

    def integrand(z):
        x = (c * z) / (1 - z)
        dxdz = c / ((1 - z) ** 2)
        return g(a, x) * dxdz

    val, _ = fixed_quad(integrand, 0, 1, n=100)
    return val

print("Gamma(3/2) =",gamma(3/2))
print("Gamma(3) [2!] =",gamma(3))
print("Gamma(6) [5!] =",gamma(6))
print("Gamma(10) [9!] =",gamma(10))

#Gamma(3/2) = 0.886226961308722
#Gamma(3) [2!] = 2.0000000000000018
#Gamma(6) [5!] = 120.00000000000009
#Gamma(10) [9!] = 362880.00000000023