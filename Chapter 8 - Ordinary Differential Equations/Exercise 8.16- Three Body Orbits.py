import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

G=1
M1 =150
M2 =200
M3 =250
def equations(t, v):
    x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3 = v

    R12 = np.hypot(x2-x1, y2-y1)
    R13 = np.hypot(x3-x1, y3-y1)
    R23 = np.hypot(x3-x2, y3-y2)

    # Star 1
    dx1dt = vx1
    dy1dt = vy1

    dvx1dt = G*M2*(x2-x1)/(R12**3) + G*M3*(x3-x1)/(R13**3)
    dvy1dt = G*M2*(y2-y1)/(R12**3) + G*M3*(y3-y1)/(R13**3)

    # Star 2
    dx2dt = vx2
    dy2dt = vy2

    dvx2dt = G*M1*(x1-x2)/(R12**3) + G*M3*(x3-x2)/(R23**3)
    dvy2dt = G*M1*(y1-y2)/(R12**3) + G*M3*(y3-y2)/(R23**3)

    # Star 3
    dx3dt = vx3
    dy3dt = vy3

    dvx3dt = G*M1*(x1-x3)/(R13**3) + G*M2*(x2-x3)/(R23**3)
    dvy3dt = G*M1*(y1-y3)/(R13**3) + G*M2*(y2-y3)/(R23**3)

    return [
    dx1dt, dy1dt,
    dx2dt, dy2dt,
    dx3dt, dy3dt,
    dvx1dt, dvy1dt,
    dvx2dt, dvy2dt,
    dvx3dt, dvy3dt
]

solution = solve_ivp(
    equations,
    [0, 2],
    [3, 1, -1, -2, -1, 1, 0, 0, 0, 0, 0, 0],
    dense_output=True
)

plt.plot(solution.y[0], solution.y[1], label="Star 1")
plt.plot(solution.y[2], solution.y[3], label="Star 2")
plt.plot(solution.y[4], solution.y[5], label="Star 3")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid()
plt.show()