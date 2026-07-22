import numpy as np
import scipy.constants as sci

a=1
L=200
totalV = 0

def V(i,j,k):
    potential = (sci.e)/((4*sci.pi*sci.epsilon_0*a*(np.sqrt(i**2+j**2+k**2))))
    if (i+j+k) % 2 == 0:
        return potential
    else:
        return -potential

for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L + 1):
            if i == j == k == 0:
                continue
            totalV+=V(i,j,k)
M=(4*sci.pi*sci.epsilon_0*a*totalV)/(sci.e)

error = 100* (np.abs(M)-1.747565)/1.747565
print("M (for NaCl):",M)
print("Error: ",error,"%")

#M (for NaCl): -1.74468504218521
#Error:  -0.16479832308326167 %