import numpy as np
import scipy.constants as sciconst
import matplotlib.pyplot as plt
from scipy.integrate import quad

a = 10 * sciconst.electron_volt
w = 5e-10
N = 100


H = np.zeros((N,N))

def Ham(m,n):

    if m==n:
        kinetic = (sciconst.hbar**2 * sciconst.pi**2 * n**2)/(2*sciconst.m_e*w**2)
        potential = a/2
    else:
        kinetic = 0
        potential = (a/np.pi**2) * (
            (((-1)**(m-n))-1)/((m-n)**2)
            -
            (((-1)**(m+n))-1)/((m+n)**2)
        )

    return kinetic + potential

for m in range(1, N+1):
    for n in range(1, N+1):
        H[m-1,n-1] = Ham(m,n)

energies, eigenvectors = np.linalg.eigh(H)
energies_ev = energies / sciconst.electron_volt
for i, e in enumerate(energies_ev):
        if i >10:
            break
        else:
            print(f"State N={i} : ", e, "eV")



def wavefunction(x, coeffs):
    psi = 0.0
    for n in range(1, N+1):
        psi += coeffs[n-1] * np.sqrt(2/w) * np.sin(np.pi*n*x/w)
    return psi

x = np.linspace(0, w, 500)
psi_gs = np.array([wavefunction(xi, eigenvectors[:, 0]) for xi in x])
psi_1 = np.array([wavefunction(xi, eigenvectors[:, 1]) for xi in x])
psi_2 = np.array([wavefunction(xi, eigenvectors[:, 2]) for xi in x])
prob = np.trapezoid(np.abs(psi_gs)**2, x)
print(f"Ground state probability integral = {prob:.6f}")


plt.plot(x, np.abs(psi_gs)**2,label ="Ground State n=0")
plt.plot(x, np.abs(psi_1)**2,label ="Ground State n=1")
plt.plot(x, np.abs(psi_2)**2,label ="Ground State n=2")
plt.xlabel("x (m)")
plt.legend()
plt.ylabel(r"$\psi(x)$")
plt.show()