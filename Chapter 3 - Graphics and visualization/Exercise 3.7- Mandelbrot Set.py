import matplotlib.pyplot as plt
import numpy as np

width = 900
height= 900
maxiter = 100

mandelbrot = np.zeros((height,width))

for i,y in enumerate(np.linspace(-2,2,width)):
    for j,x in enumerate(np.linspace(-2,2,height)):
        c = x + (y*1j)
        z=0
        for n in range(maxiter):
            z = z*z + c
            if np.abs(z) > 2:
                mandelbrot[i,j] = n
                break
        else:
            mandelbrot[i,j] = maxiter

plt.imshow(mandelbrot)
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()

