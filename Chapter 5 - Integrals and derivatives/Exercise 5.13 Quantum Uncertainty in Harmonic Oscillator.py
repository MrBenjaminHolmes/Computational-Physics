from scipy.integrate import fixed_quad
import scipy.constants as constant
import scipy.special as spec
import numpy as np
import matplotlib.pyplot as plt

def h(n,x):
    if n == 0:
        return 1
    if n == 1:
        return 2*x
    return 2*x*h(n-1,x) - 2*(n-1)*h(n-2,x)

def psi(n,x):
    a = (1)/(np.sqrt((2**n)*spec.factorial(n)*np.sqrt(np.pi)))
    b = np.exp((-x**2)/2)
    c= h(n,x)
    return a*b*c

x_vals = np.linspace(-4,4,100)

psi0 = [psi(0, x) for x in x_vals]

psi1 = [psi(1, x) for x in x_vals]

psi2 = [psi(2, x) for x in x_vals]

psi3 = [psi(3, x) for x in x_vals]

#plt.plot(x_vals,psi0 , label = "$\psi_0$")
#plt.plot(x_vals,psi1 , label = "$\psi_1$")
#plt.plot(x_vals,psi2 , label = "$\psi_2$")
#plt.plot(x_vals,psi3 , label = "$\psi_3$")
#plt.legend()
#plt.show()

x_vals = np.linspace(-10,10,100)
psilst = [psi(30, x) for x in x_vals]
plt.plot(x_vals,psilst)
plt.show()