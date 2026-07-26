import numpy as np

def f(x):
    return np.sin(np.sqrt(100*x))**2

def trapeziumRule(a, b, N, f):

    h = (b - a) / N

    total = f(a) + f(b)

    for i in range(1, N):
        x = a + i * h
        total += 2 * f(x)

    integral = (h / 2) * total
    return integral


N = 1
epsilon = 1e-6
e_epsilon = 1

while e_epsilon > epsilon:

    T_N = trapeziumRule(0, 1, N, f)
    T_2N = trapeziumRule(0, 1, 2*N, f)

    e_epsilon = abs(T_N - T_2N) / 3

    print("Approximate integral, N =", N, "=", T_N)
    print("Estimated Error =", e_epsilon)

    N *= 2