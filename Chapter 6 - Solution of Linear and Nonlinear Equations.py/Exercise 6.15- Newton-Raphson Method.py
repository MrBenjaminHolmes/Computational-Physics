import numpy as np 
import matplotlib.pyplot as plt

accuracy = 1e-11

def P(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 +420*x**2 -42*x + 1

def ddx(x):
    return 5544*x**5 - 13860*x**4 + 12600*x**3 - 5040*x**2 + 840*x - 42

xvals = np.linspace(0,1,1000)
pvals = [P(x) for x in xvals]
plt.plot(xvals,pvals)
plt.grid()
plt.show()

startingpoints = [0.03,0.17,0.38,0.6,0.82,0.96]
roots = []
for point in startingpoints:
    x= point
    delta = 1
    while abs(delta)>accuracy:
        delta = (P(x))/(ddx(x))  
        x-= delta
    roots.append(x)

print(roots)