from scipy.integrate import fixed_quad
import scipy.constants as constant
import numpy as np

def f(x):
    return np.where(x > 700, 0.0, x**3 / np.expm1(x))

integrand = lambda z: f(z / (1-z)) / (1-z)**2

s,_ = fixed_quad(integrand, 0, 1, n=50)

stephanBoltzmannConstant = (constant.Boltzmann**4)/(4*constant.pi**2 * constant.c**2 * constant.hbar**3) * s
errorSB= (stephanBoltzmannConstant-constant.Stefan_Boltzmann)/(constant.Stefan_Boltzmann) *100
print(f"Stephan-Boltzmann Constant = {stephanBoltzmannConstant}, error % = {errorSB}")


#Stephan-Boltzmann Constant = 5.670374417654671e-08, error % = -2.697812490399007e-08