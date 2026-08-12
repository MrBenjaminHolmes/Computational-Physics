import numpy as np 
import matplotlib.pyplot as plt

N = 1000

def f(t):
    if np.floor(2*t) % 2 == 0:
        return 1
    else:
        return -1

xvals = np.linspace(0,N-1)
y = [f(x) for x in xvals/1000]

c = np.fft.rfft(y)
y_filtered = np.fft.irfft(c, n=len(y))
c[10:] = 0

y_filtered = np.fft.irfft(c, n=len(y))

plt.plot(y, label="Original")
plt.plot(y_filtered, label="First 10 coefficients")
plt.legend()
plt.show()