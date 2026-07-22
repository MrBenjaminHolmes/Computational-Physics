import matplotlib.pyplot as plt
import numpy as np

# Sin Curve
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)

# Deltoid Curve
theta = np.linspace(0, 2*np.pi, 100)
x2 = 2*np.cos(theta) + np.cos(2*theta)
y2 = 2*np.sin(theta) - np.sin(2*theta)

# Galilean Spiral
theta = np.linspace(0, 10*np.pi, 1000)
r = theta**2
x3 = r*np.cos(theta)
y3 = r*np.sin(theta)

# Fey's Function
theta = np.linspace(0, 24*np.pi, 10000)
r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) + np.sin(theta/12)**5
x4 = r*np.cos(theta)
y4 = r*np.sin(theta)


fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0,0].plot(x1, y1, color="blue")
axs[0,0].set_title("Sin Curve")

axs[0,1].plot(x2, y2, color="orange")
axs[0,1].set_title("Deltoid Curve")

axs[1,0].plot(x3, y3, color="green")
axs[1,0].set_title("Galilean Spiral")

axs[1,1].plot(x4, y4, color="red")
axs[1,1].set_title("Fey's Function")


for ax in axs.flat:
    ax.grid(True)
    ax.set_aspect("equal")


plt.show()