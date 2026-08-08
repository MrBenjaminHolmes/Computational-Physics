import numpy as np 
import matplotlib.pyplot as plt
c=0.00
accuracy = 1e-6


def f(x):
    return 1-np.exp(-c*x)

def ddx(x):
    return c*np.exp(-c*x)

solutions = []
xlst = np.linspace(0, 3, 301)
while c < 3.00:
    error = 1e10
    x = 1
    xvalues = [x]
    while (error > accuracy):
        x = f(x)
        xvalues.append(x)
        error = (xvalues[-1]-xvalues[-2])/(1-(1)/(ddx(x)))
    solutions.append(x)
    c+=0.01

plt.plot(xlst,solutions)
plt.xlabel("C Value")
plt.ylabel("Solution")
plt.title("Relaxation Method For "+r"$ x=1-e^{-cx}$")
plt.show()