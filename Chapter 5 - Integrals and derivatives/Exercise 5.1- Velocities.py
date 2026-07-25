import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("Resources/velocities.txt", float)
time = data[:,0]
vel = data[:,1]

N=len(time)
a=time[0]
b=time[-1]
h=1
s=0.5*vel[0] + 0.5*vel[-1]
dist = [s]

for k in range(1,N):
    s+=vel[k]
    dist.append(s)

print("Distance (m):",s,)


plt.plot(time,vel)
plt.plot(time,dist)
plt.legend(['Velocity', 'Displacement'])
plt.grid(True)
plt.title("Velocities/Displacement Data")
plt.show()