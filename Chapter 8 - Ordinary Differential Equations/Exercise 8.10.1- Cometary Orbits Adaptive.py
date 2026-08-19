import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G
import time

Mass = 1.9884099e30

a = 0
b = 4.8e9

# Target accuracy: 1 km/year
delta = 1000 / (365.25 * 24 * 3600)

def OrbitFODE(r, t):
    x = r[0]
    alpha = r[1]
    y = r[2]
    beta = r[3]

    d = np.sqrt(x**2 + y**2)

    fx = alpha
    falpha = -G * Mass * x / d**3
    fy = beta
    fbeta = -G * Mass * y / d**3

    return np.array([fx, falpha, fy, fbeta], float)


def RK4step(r, t, h):
    k1 = h * OrbitFODE(r, t)
    k2 = h * OrbitFODE(r + 0.5*k1, t + 0.5*h)
    k3 = h * OrbitFODE(r + 0.5*k2, t + 0.5*h)
    k4 = h * OrbitFODE(r + k3, t + h)

    return r + (k1 + 2*k2 + 2*k3 + k4) / 6

def adaptiveRK4(init, h_initial):
    t=a
    r=np.array(init,dtype=float)
    tpoints = []
    xpoints = []
    ypoints = []
    hpoints = []

    h = h_initial
    while t < b:

        # Don't step past the end
        if t + h > b:
            h = b - t

        # One RK4 step of size h
        r1 = RK4step(r, t, h)

        # Two RK4 steps of size h/2
        rm = RK4step(r, t, h/2)
        r2 = RK4step(rm, t + h/2, h/2)

        # Estimate position error
        error = np.sqrt(
            (r1[0] - r2[0])**2 +
            (r1[2] - r2[2])**2
        ) / 15

        # Accept step if accuracy is good enough
        if error <= delta * h:

            t += h
            r = r2

            tpoints.append(t)
            xpoints.append(r[0])
            ypoints.append(r[2])
            hpoints.append(h)

            # Increase/decrease step size
            if error == 0:
                factor = 2
            else:
                factor = 0.9 * (delta * h / error)**(1/5)

            h = h * min(2, max(0.5, factor))

        else:
            # Error too large: reduce step size and try again
            factor = 0.9 * (delta * h / error)**(1/5)
            h = h * max(0.1, factor)

    return tpoints, xpoints, ypoints, hpoints


start = time.time()

orbit = adaptiveRK4([4e12, 0, 0, 500], 1e6)

end = time.time()

print("Calculation time:", end - start, "seconds")
print("Number of accepted steps:", len(orbit[0]))
print("Minimum h:", min(orbit[3]), "seconds")
print("Maximum h:", max(orbit[3]), "seconds")

plt.plot(orbit[1], orbit[2])
plt.plot(orbit[1], orbit[2], '.', markersize=2)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Cometary Orbit - Adaptive RK4")
plt.axis("equal")
plt.show()

plt.plot(orbit[0], orbit[3])
plt.xlabel("Time (s)")
plt.ylabel("Step size h (s)")
plt.title("Adaptive Step Size")
plt.show()


