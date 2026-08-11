import matplotlib.pyplot as plt
import numpy as np

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

data = np.loadtxt("Resources/sunspots.txt", float)
x = data[:,0]
y = data[:,1]
c = dft(y)
powerSpec = abs(c)**2

fig, ax = plt.subplots(2)

ax[0].plot(x,y)
N = len(y)
freq = np.arange(N // 2 + 1) / N

ax[1].plot(freq, powerSpec)
ax[1].set_xlabel("Frequency")
ax[1].set_ylabel("Power")
plt.tight_layout()
plt.show()

period = 1 / 0.007635
print(period)
#130.97576948264572 months