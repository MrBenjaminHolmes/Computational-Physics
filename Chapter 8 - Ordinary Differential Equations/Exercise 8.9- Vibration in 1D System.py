import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Parameters
m = 1.0
k = 6.0
omega = 2.0
N = 5

# Time interval
t0 = 0.0
t_end = 20.0
h = 0.01

nsteps = int((t_end - t0) / h)
t = np.linspace(t0, t_end, nsteps + 1)
r = np.zeros(2 * N)

solution = np.zeros((nsteps + 1, 2 * N))
solution[0] = r

def f(r,t):
    xi = r[:N]
    v = r[N:]
    drdt = np.zeros(2 * N)
    drdt[:N] = v
    F = np.zeros(N)
    F[0] = np.cos(omega * t)
    drdt[N] = (k / m) * (xi[1] - xi[0]) + F[0] / m
    for i in range(1, N - 1):
        drdt[N + i] = (
            (k / m) * (xi[i + 1] + xi[i - 1] - 2 * xi[i])
            + F[i] / m
        )
    
    drdt[2 * N - 1] = (
        (k / m) * (xi[N - 2] - xi[N - 1])
        + F[N - 1] / m
    )
    
    return drdt



nsteps = int((t_end - t0) / h)
t = np.linspace(t0, t_end, nsteps + 1)
r = np.zeros(2 * N)

# Fourth-order Runge-Kutta method
for j in range(nsteps):
    rj = solution[j]
    tj = t[j]
    
    k1 = f(rj, tj)
    k2 = f(rj + 0.5 * h * k1, tj + 0.5 * h)
    k3 = f(rj + 0.5 * h * k2, tj + 0.5 * h)
    k4 = f(rj + h * k3, tj + h)
    
    solution[j + 1] = rj + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)


# Plot all displacements
for i in range(N):
    plt.plot(t, solution[:, i], label=fr'$\xi_{i+1}$')

plt.xlabel('Time $t$')
plt.ylabel('Displacement')
plt.title(f'Motion of {N} masses')
plt.legend()
plt.grid()
plt.show()


fig, ax = plt.subplots(figsize=(12, 2))

# Equilibrium positions
rest = np.arange(N, dtype=float)

ax.set_xlim(-1, N)
ax.set_ylim(-0.5, 0.5)
ax.set_yticks([])
ax.set_xlabel("Position")
ax.set_title("Coupled mass-spring system")

# Lines connecting masses
spring, = ax.plot([], [], 'k-', lw=1.5)

# Masses
masses, = ax.plot([], [], 'o', markersize=12)


def update(frame):

    displacement = solution[frame, :N]

    xpos = rest + displacement
    ypos = np.zeros(N)
    spring.set_data(xpos, ypos)
    masses.set_data(xpos, ypos)

    ax.set_title(
        f"Coupled mass-spring system, t = {t[frame]:.2f}"
    )

    return spring, masses

frames = range(0, nsteps + 1, 5)

ani = FuncAnimation(
    fig,
    update,
    frames=frames,
    interval=20,
    blit=True
)

plt.show()