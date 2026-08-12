import numpy as np
import matplotlib.pyplot as plt

# Physical parameters
w = 200e-6
W = 10 * w
lam = 500e-9
f = 1.0
N = 2**14
alpha = np.pi / (20e-6)

u = np.linspace(-W/2, W/2, N, endpoint=False)
inside = np.abs(u) <= w/2
q = np.zeros(N)
q[inside] = np.sin(alpha * u[inside])**2

y=np.sqrt(q)
c = np.fft.fft(y)
I = (W**2 / N**2) * np.abs(c)**2
x = np.fft.fftfreq(N, d=W/N) * lam * f
x = np.fft.fftshift(x)
I = np.fft.fftshift(I)
mask = (x >= -0.05) & (x <= 0.05)
x_screen = x[mask]
I_screen = I[mask]

diffractionPattern = np.tile( I_screen, (800, 1))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))
ax1.imshow(
    diffractionPattern,
    cmap="gray",
    aspect="auto",
    vmax=np.max(diffractionPattern) * 0.2
)
ax1.set_ylabel("Height")
ax1.set_title("Diffraction Pattern")

ax2.plot(x_screen * 100, I_screen)
ax2.set_xlabel("Position x (mm)")
ax2.set_ylabel("Relative intensity")
ax2.set_title("Intensity Profile")

plt.tight_layout()
plt.show()