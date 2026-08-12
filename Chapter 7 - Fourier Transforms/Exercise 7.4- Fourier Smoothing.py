import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("Resources/dow.txt", float)

c = np.fft.rfft(data)
c[int(0.02 * len(c)):] = 0

fx = np.fft.irfft(c)

plt.plot(data)
plt.plot(fx)
plt.show()