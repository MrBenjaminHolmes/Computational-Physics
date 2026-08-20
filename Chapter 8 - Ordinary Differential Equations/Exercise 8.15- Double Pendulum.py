import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m=1
g= 9.80665
l=0.4

def equations(t, y):
    theta1, theta2, w1, w2 = y

    dytheta1dt = w1
    dytheta2dt = w2

    a =  (w1**2 * np.sin((2*theta1) - (2*theta2))) + (2*w2**2* np.sin(theta1-theta2)) + ((g/l)*(np.sin(theta1-(2*theta2))+3*np.sin(theta1)))
    b = (4*(w1**2) * np.sin((theta1) - (theta2))) + (w2**2* np.sin((2*theta1) - (2*theta2))) + (2*(g/l)*(np.sin((2*theta1)-(theta2))-np.sin(theta2)))    
    c = 3-np.cos((2*theta1) - (2*theta2))

    dyw1dt = -(a)/(c)
    dyw2dt = (b)/(c)

    return [dytheta1dt, dytheta2dt, dyw1dt, dyw2dt]

solution = solve_ivp(
    equations,
    [0, 100],  
    [np.deg2rad(80), np.deg2rad(110), 0, 0],
    dense_output=True
)


plt.plot(solution.t, solution.y[0], label="θ1")
plt.plot(solution.t, solution.y[1], label="θ2")
plt.plot(solution.t, solution.y[2], label="w1")
plt.plot(solution.t, solution.y[3], label="w2")

plt.xlabel("t")
plt.ylabel("solution")
plt.legend()
plt.show()

fps = 60
t_eval = np.linspace(0, 100, 100 * fps)
y_eval = solution.sol(t_eval)

fig, ax = plt.subplots()
L_total = 2 * l
ax.set_xlim(-L_total * 1.2, L_total * 1.2)
ax.set_ylim(-L_total * 1.2, L_total * 1.2)
ax.set_aspect('equal')
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Double Pendulum")

rod1, = ax.plot([], [], 'o-', lw=3, color='tab:blue')
bob1, = ax.plot([], [], 'o', markersize=12, color='tab:blue')
rod2, = ax.plot([], [], 'o-', lw=3, color='tab:orange')
bob2, = ax.plot([], [], 'o', markersize=12, color='tab:orange')

def update(frame):
    theta1 = y_eval[0][frame]
    theta2 = y_eval[1][frame]  

    x1 = l * np.sin(theta1)
    y1 = -l * np.cos(theta1)

    x2 = x1 + l * np.sin(theta2)
    y2 = y1 - l * np.cos(theta2)

    rod1.set_data([0, x1], [0, y1])
    bob1.set_data([x1], [y1])
    rod2.set_data([x1, x2], [y1, y2])
    bob2.set_data([x2], [y2])
    
    return rod1, bob1, rod2, bob2

animation = FuncAnimation(
    fig,
    update,
    frames=len(t_eval),
    interval=500/fps,  
    blit=True
)

plt.show()