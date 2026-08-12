import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Resources/pitch.txt", float)

def fft(y):
    N = len(y)

    if N == 1:
        return y

    even = fft(y[0::2])
    odd = fft(y[1::2])
    X = [0] * N

    for k in range(N // 2):
        W = np.exp(-2j * np.pi * k / N)

        X[k] = even[k] + W * odd[k]
        X[k + N // 2] = even[k] - W * odd[k]

    return X

fftData = fft(data)

plt.plot(np.abs(fftData))
plt.show()