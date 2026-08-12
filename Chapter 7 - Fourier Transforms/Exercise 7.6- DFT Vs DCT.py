import matplotlib.pyplot as plt
import numpy as np
import scipy
data = np.loadtxt("Resources/dow2.txt", float)

c = np.fft.rfft(data)
c[int(0.02 * len(c)):] = 0

fx = np.fft.irfft(c)

plt.plot(data)
plt.plot(fx)
plt.show()

data = np.loadtxt("Resources/dow2.txt", float)

c = scipy.fft.dct(data)
c[int(0.02 * len(c)):] = 0

fx = scipy.fft.idct(c)

plt.plot(data)
plt.plot(fx)
plt.show()