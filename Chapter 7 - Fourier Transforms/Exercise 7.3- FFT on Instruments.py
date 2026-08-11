import numpy as np
import matplotlib.pyplot as plt

pianoData = np.loadtxt("Resources/piano.txt", float)
trumpetData = np.loadtxt("Resources/trumpet.txt", float)


cPiano = np.fft.fft(pianoData)
cTrumpet = np.fft.fft(trumpetData)

magPiano = np.abs(cPiano[:10000])
magTrumpet = np.abs(cTrumpet[:10000])

plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 1)
plt.plot(magPiano, color='blue')
plt.title("Piano Fourier Coefficients (First 10,000)")
plt.ylabel("Magnitude")

plt.subplot(2, 1, 2)
plt.plot(magTrumpet, color='orange')
plt.title("Trumpet Fourier Coefficients (First 10,000)")
plt.xlabel("Coefficient Index (k)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()

N = len(pianoData)
sampling_rate = 44100
k_peak_piano = np.argmax(magPiano[1:]) + 1
freq_piano = (k_peak_piano * sampling_rate) / N
k_peak_trumpet = np.argmax(magTrumpet[1:]) + 1
k_peak_trumpet = (k_peak_trumpet * sampling_rate) / N


print(f"Peak Index Piano (k): {k_peak_piano}")
print(f"Fundamental Frequency Piano: {freq_piano:.2f} Hz")
print(f"Peak Index Trumpet (k): {k_peak_trumpet}")
print(f"Fundamental Frequency Trumpet: {k_peak_trumpet:.2f} Hz")

#Peak Index Piano (k): 1190
#Fundamental Frequency Piano: 524.79 Hz
#Peak Index Trumpet (k): 1043.847
#Fundamental Frequency Trumpet: 1043.85 Hz