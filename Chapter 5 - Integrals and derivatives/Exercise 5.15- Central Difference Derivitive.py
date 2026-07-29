import numpy as np 
import matplotlib.pyplot as plt

def f(x):
    return 1+np.tanh(2*x)/2

h=0.0001
x = np.linspace(-2,2,1000)

dfdx = ((f(x+h/2))-(f(x-h/2)))/h


plt.plot(x,1 / np.cosh(2*x)**2)
plt.plot(x,dfdx , '--')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()