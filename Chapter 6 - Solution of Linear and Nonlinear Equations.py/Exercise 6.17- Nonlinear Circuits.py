import numpy as np

# Constants
Vp = 5.0

R1 = 1e3
R2 = 4e3
R3 = 3e3
R4 = 2e3

I0 = 3e-9
VT = 0.05


# The two equations
def f(V):
    V1, V2 = V

    diode = I0 * (np.exp((V1 - V2) / VT) - 1)

    f1 = (Vp - V1) / R1 - V1 / R2 - diode
    f2 = (Vp - V2) / R3 - V2 / R4 + diode

    return np.array([f1, f2])


# Jacobian
def jacobian(V):
    V1, V2 = V

    A = I0 / VT * np.exp((V1 - V2) / VT)

    J = np.array([
        [-1/R1 - 1/R2 - A,  A],
        [A,                 -1/R3 - 1/R4 - A]
    ])

    return J


# Initial guess
V = np.array([3.4, 2.9])


# Newton's method
for i in range(100):

    F = f(V)
    J = jacobian(V)

    # Solve J * delta = -F
    delta = np.linalg.solve(J, -F)

    V = V + delta

    # Check convergence
    if np.linalg.norm(delta) < 1e-10:
        break


print("Iterations:", i + 1)
print("V1 =", V[0], "V")
print("V2 =", V[1], "V")

print("f1 =", f(V)[0])
print("f2 =", f(V)[1])
print(V[0]-V[1])