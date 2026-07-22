import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("Resources/sunspots.txt", float)

r = 5
x = data[:,0]
y = data[:,1]

average = []

for i in range(r, 1000-r):
    ave = 0.0
    
    for m in range(-r, r+1):
        ave += y[i+m]
    
    ave /= (2*r+1)
    average.append(ave)

plt.plot(x[r:1000-r], average)
plt.plot(x[:1000], y[:1000])

plt.show()