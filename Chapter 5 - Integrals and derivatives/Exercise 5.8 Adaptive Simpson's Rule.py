import numpy as np

def f(x):
    return np.sin(np.sqrt(100*x))**2

a = 0.0
b = 1.0
epsilon = 1e-6

N = 2
h = (b-a)/N
S = (f(a) + f(b))/3
T = 2/3 * sum(f(a + k*h) for k in range(1, N, 2))
I = h*(S + 2*T)
print(f"N = {N}, I ={I}")
error = 1.0

while abs(error) > epsilon:

    I_old = I

    N = 2*N
    h = (b-a)/N

    T_new = 2/3 * sum(f(a + k*h) for k in range(1, N, 2))
    S = S + T
    T = T_new

    # Eq. (5.39)
    I = h*(S + 2*T)

    error = (I - I_old)/15

    print(f"N = {N}, I ={I}, Error = {error}")

#N = 2, I =0.38431604889308213
#N = 4, I =0.5746331650289503, Error = 0.012687807742391215
#N = 8, I =0.36656898106322056, Error = -0.013870945597715319
#N = 16, I =0.4391386762335798, Error = 0.004837979678023951
#N = 32, I =0.45451843128504427, Error = 0.0010253170034309625
#N = 64, I =0.45574568635801116, Error = 8.181700486445954e-05
#N = 128, I =0.4558270287586108, Error = 5.422826706643254e-06
#N = 256, I =0.45583218714672064, Error = 3.438925406551441e-07