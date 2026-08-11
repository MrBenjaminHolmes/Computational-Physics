import numpy as np 
import matplotlib.pyplot as plt

N=1000

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

def square(n):
    if n/N <= 0.5:
        return 1.0
    else:
        return 0.0

def saw(n):
    return n 

def sin(n):
    return (np.sin((np.pi*n)/(N)))*(np.sin((20*np.pi*n)/(N)))


xvals = np.arange(N)
ysqaure = np.array([square(x) for x in xvals])
ysaw = np.array([saw(x) for x in xvals])
ysin = np.array([sin(x) for x in xvals])

csquare = dft(ysqaure)
csaw = dft(ysaw)
csin= dft(ysin)

fig, ax = plt.subplots(3)

ax[0].plot(np.abs(csquare))
ax[0].set_title("Sqaure Wave")
ax[1].plot(np.abs(csaw))
ax[1].set_title("Saw Wave")
ax[2].plot(np.abs(csin))
ax[2].set_title("Modulated Sin Wave")

plt.title("DFT of Simple Functions")
plt.tight_layout()
plt.show()