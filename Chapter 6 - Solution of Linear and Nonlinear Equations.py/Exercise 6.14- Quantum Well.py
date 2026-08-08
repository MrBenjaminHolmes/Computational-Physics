import numpy as np
import scipy.constants as sci
import matplotlib.pyplot as plt

V = 20 * sci.electron_volt
w = 1e-9


def y1(E):
    k = np.sqrt(2*sci.m_e*E)/sci.hbar
    return np.tan(k*w/2)

def y2(E):
    return np.sqrt((V-E)/E)

def y3(E):
    return -np.sqrt(E/(V-E))

# Plot curves
E_plot = np.linspace(1e-6*V, 0.999999*V, 1000)

plt.figure(figsize=(8,6))
plt.plot(E_plot/sci.electron_volt, y1(E_plot), label=r'$\tan(kw/2)$')
plt.plot(E_plot/sci.electron_volt, y2(E_plot), label=r'$\sqrt{(V-E)/E}$')
plt.plot(E_plot/sci.electron_volt, y3(E_plot), label=r'$-\sqrt{E/(V-E)}$')
plt.ylim(-10,10)
plt.xlabel("Energy (eV)")
plt.ylabel("Value")
plt.legend()
plt.show()

import numpy as np
import scipy.constants as sci

# Parameters
V = 20 * sci.electron_volt
w = 1e-9


# Define equations
def even(E):
    k = np.sqrt(2*sci.m_e*E)/sci.hbar
    return np.tan(k*w/2) - np.sqrt((V-E)/E)


def odd(E):
    k = np.sqrt(2*sci.m_e*E)/sci.hbar
    return np.tan(k*w/2) + np.sqrt(E/(V-E))


# Bisection function
def bisection(f, a, b, tol=1e-12):

    fa = f(a)
    fb = f(b)

    while abs(b-a) > tol:
        c = (a+b)/2
        fc = f(c)

        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a+b)/2


E_values = np.linspace(1e-8*V, 0.999999*V, 10000)

states = []

for i in range(len(E_values)-1):

    try:
        if even(E_values[i])*even(E_values[i+1]) < 0:
            E = bisection(even, E_values[i], E_values[i+1])
            states.append((E, "even"))
    except:
        pass


    try:
        if odd(E_values[i])*odd(E_values[i+1]) < 0:
            E = bisection(odd, E_values[i], E_values[i+1])
            states.append((E, "odd"))
    except:
        pass


states_sorted = sorted(states, key=lambda x:x[0])

unique_states = []

for E, parity in states_sorted:
    if len(unique_states)==0 or abs(E-unique_states[-1][0]) > 1e-6*sci.electron_volt:
        unique_states.append((E, parity))

print("First 6 energy levels:")
for n, (E, parity) in enumerate(unique_states[:6], start=1):
    print(f"n={n}: {E/sci.electron_volt:.6f} eV ({parity})")