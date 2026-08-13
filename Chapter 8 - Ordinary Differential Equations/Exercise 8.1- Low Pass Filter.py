import numpy as np
import matplotlib.pyplot as plt

def Vin(t):
    if np.floor(2*t) % 2 == 0:
        return 1
    else:
        return -1

def f(Vout,t,rc):
    return (1/rc) * (Vin(t)-Vout)

a=0
b=10
N=100000
h=(b-a)/N

RC_VALUES= [0.01,0.1,1]

for RC in RC_VALUES:
    Vout = 0
    tpoints = np.arange(a,b,h)
    Voutpoints = []
    for t in tpoints:
        Voutpoints.append(Vout)
        k1=h*f(Vout,t,RC)
        k2= h*f(Vout+0.5*k1,t+0.5*h,RC)
        k3 = h*f(Vout+0.5*k2,t+0.5*h,RC)
        k4 = h*f(Vout+k3,t+h,RC)
        Vout+= (k1+2*k2+2*k3+k4)/6

    plt.plot(tpoints, Voutpoints, label=f"RC = {RC}")

plt.xlabel("Time, t")
plt.ylabel("$V_{out}$")
plt.title("Output of a Low-Pass Filter")
plt.grid(True)
plt.legend()
plt.xlim(0, 10)

plt.show()
