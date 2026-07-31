import numpy as np
import matplotlib.pyplot as plt

R = [1000,2000,1000,2000,1000,2000]
C1 = 1e-6
C2= 0.5e-6
X_plus = 3
w = 1000

A = np.array([
    [(1/R[0] + 1/R[3]+ 1j*w*C1),(1j*w*C1),0],
    [(-1j*w* C1),(1/R[1] +1/R[4]+ 1j*w*C1 + 1j*w*C2),(-1j*w*C2)],
    [0, (-1j*w*C2), (1/R[2] + 1/R[5] + 1j*w*C2)]
])

v = np.array([X_plus/R[0], X_plus/R[1], X_plus/R[2]])

x = np.linalg.solve(A,v)

print(x)
t= np.linspace(0,0.05,1000)

V_plus = X_plus*np.exp(1j*w*t)
V1= x[0]*np.exp(1j*w*t)
V2= x[1]*np.exp(1j*w*t)
V3= x[2]*np.exp(1j*w*t)

plt.plot(t,V_plus,label="V+")
plt.plot(t,V1,label="V1")
plt.plot(t,V2, label="V2")
plt.plot(t,V3,label="V3")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid()
plt.show()