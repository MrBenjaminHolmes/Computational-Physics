import numpy as np 
import matplotlib.pyplot as plt

def f(m,x,theta):
    return np.cos(m*theta - x*np.sin(theta))

def j(m,x):
    N = 1000
    h = np.pi/N

    I =f(m,x,0)+f(m,x,np.pi)

    for i in range(1,N,2):
        I += 4 * f(m,x,np.pi - i*h)

    for i in range(2,N,2):
        I += 2 * f(m,x,np.pi - i*h)

    I *= h/3 
    return 1/np.pi * I

x_vals = np.linspace(0, 20, 100)

J1 = [j(0, x) for x in x_vals]
print("J1 COMPLETE...")
J2 = [j(1, x) for x in x_vals]
print("J2 COMPLETE...")
J3 = [j(2, x) for x in x_vals]
print("J3 COMPLETE...")

plt.plot(x_vals, J1, label="J0")
plt.plot(x_vals, J2, label="J1")
plt.plot(x_vals, J3, label="J2")

plt.grid(True)
plt.legend()
plt.title("Bessel Functions")
plt.xlabel("x")
plt.ylabel("J_m(x)")
plt.show()