import numpy as np
import matplotlib.pyplot as plt

h = 0.001
tmax = 50
N = int(tmax / h)

t = np.linspace(0, tmax, N + 1)
x = np.zeros(N + 1)
v = np.zeros(N + 1)

xhalf = np.zeros(N)
vhalf = np.zeros(N)


x[0] = 1.0
v[0] = 0.0

xhalf[0] = x[0] + (h/2)*v[0]

vhalf[0] = v[0] + (h/2)*(v[0]**2 - x[0] - 5)

for n in range(N - 1):

    x[n+1] = x[n] + h*vhalf[n]

    v[n+1] = v[n] + h*(vhalf[n]**2 - xhalf[n] - 5)

    xhalf[n+1] = xhalf[n] + h*v[n+1]

    vhalf[n+1] = vhalf[n] + h*(v[n+1]**2 - x[n+1] - 5)

plt.plot(t, x)

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Leapfrog solution")

plt.grid()
plt.show()