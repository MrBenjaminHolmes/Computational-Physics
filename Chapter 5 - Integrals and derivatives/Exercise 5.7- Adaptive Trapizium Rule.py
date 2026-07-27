import numpy as np

def f(x):
    return np.sin(np.sqrt(100*x))**2


def trapeziumRule(a, b, N, f):
    h = (b - a) / N

    total = f(a) + f(b)

    for i in range(1, N):
        total += 2 * f(a + i * h)

    return (h / 2) * total


N = 1
epsilon = 1e-6
e_epsilon = 1

T_N = trapeziumRule(0, 1, N, f)

while abs(e_epsilon) > epsilon:

    N_new = 2 * N
    h_new = (1 - 0) / N_new

    new_points = 0

    for i in range(1, N + 1):
        x = 0 + (2*i - 1) * h_new
        new_points += f(x)

    T_2N = 0.5 * T_N + h_new * new_points

    e_epsilon = abs(T_N - T_2N) / 3

    print("Approximate integral, N =", N, "=", T_N)
    print("Estimated Error =", e_epsilon)

    T_N = T_2N
    N = N_new

#Approximate integral, N = 1 = 0.147979484546652
#Estimated Error = 0.05908414108660753
#Approximate integral, N = 2 = 0.3252319078064746
#Estimated Error = 0.06235031430561896
#Approximate integral, N = 4 = 0.5122828507233315
#Estimated Error = 0.03642846741502772
#Approximate integral, N = 8 = 0.4029974484782483
#Estimated Error = 0.009035306938832885
#Approximate integral, N = 16 = 0.43010336929474696
#Estimated Error = 0.0061037654975743165
#Approximate integral, N = 32 = 0.4484146657874699
#Estimated Error = 0.0018327551426352933
#Approximate integral, N = 64 = 0.4539129312153758
#Estimated Error = 0.000478524385808754
#Approximate integral, N = 128 = 0.45534850437280205
#Estimated Error = 0.00012092069347964991
#Approximate integral, N = 256 = 0.455711266453241
#Estimated Error = 3.0311066141042176e-05
#Approximate integral, N = 512 = 0.45580219965166413
#Estimated Error = 7.582826918613635e-06
#Approximate integral, N = 1024 = 0.45582494813241997
#Estimated Error = 1.8960230755427077e-06
#Approximate integral, N = 2048 = 0.4558306362016466
#Estimated Error = 4.74025541467397e-07