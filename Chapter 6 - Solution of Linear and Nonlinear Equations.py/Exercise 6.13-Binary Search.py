import numpy as np
import scipy.constants as scicon

def f(x):
    return (5*np.exp(-x)) + (x) - (5)

x1 =4
x2=6

fx1 = f(x1)
fx2 = f(x2)

accuracy = 1e-10

while np.abs(x1-x2) > accuracy:
    x_new = (x1+x2)/2
    fxnew = f(x_new)
    if fxnew * fx1 > 0:
        x1 = x_new
        fx1 = fxnew
    if fxnew * fx2 > 0:
        x2 = x_new
        fx2 = fxnew

x = (x1+x2)/2
weinsConstant = (scicon.h *scicon.c)/(scicon.Boltzmann*x)
print("Weins Constant: ",weinsConstant)
print("Suns Temperature: ", weinsConstant/502e-9,"K")