import numpy as np 
import matplotlib.pyplot as plt
λ = 500e-9
k= (np.pi*2)/λ
width = 200
height= 200
density = np.zeros((height,width))
def f(m,x,theta):
    return np.cos(m*theta - x*np.sin(theta))

def j_func(m,x):
    N = 1000
    h = np.pi/N

    I =f(m,x,0)+f(m,x,np.pi)

    for i in range(1,N,2):
        I += 4 * f(m,x,np.pi - i*h)

    for i in range(2,N,2):
        I += 2 * f(m,x,np.pi - i*h)

    I *= h/3 
    return 1/np.pi * I

def I(r):
    if r == 0:
        return 0.25
    return ((j_func(1,(k*r)))/(k*r))**2

for i,y in enumerate(np.linspace(-1e-6,1e-6,width)):
    for j,x in enumerate(np.linspace(-1e-6,1e-6,height)):
           r = R = np.sqrt(x**2 + y**2)
           density[i,j] = I(r)

plt.imshow(density, vmax=0.01, cmap='inferno')
plt.colorbar(label="Intensity")
plt.show()