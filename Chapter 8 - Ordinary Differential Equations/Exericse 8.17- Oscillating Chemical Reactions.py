import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

a = 1
b = 3

def equations(t, y):
    dxdt = 1 - ((b + 1) * y[0]) + a * (y[0]**2) * y[1]
    dydt = b * y[0] - a * (y[0]**2) * y[1]
    return [dxdt, dydt]


t_eval = np.linspace(0, 20, 1000)

solution = solve_ivp(
    equations,
    [0, 20],
    [0, 0],
    t_eval=t_eval
)

plt.plot(solution.t, solution.y[0], label="x")
plt.plot(solution.t, solution.y[1], label="y")

plt.xlabel("t")
plt.ylabel("solution")
plt.legend()
plt.show()