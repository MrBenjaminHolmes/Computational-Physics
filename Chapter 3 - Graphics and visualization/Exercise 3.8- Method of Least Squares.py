import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as sci
data = np.loadtxt("Resources/millikan.txt", float)

x = data[:,0]
y = data[:,1]

ex = 1/(len(x))*sum(x)
ey = 1/(len(y))*sum(y)
exx= 1/(len(x))* sum(x**2)
exy= 1/(len(y))* sum(y*x)

m = (exy-(ex*ey))/(exx-(ex*ex))
c = ((exx*ey) - (ex*exy))/(exx-(ex*ex))

plt.scatter(x,y)
plt.plot(x,m*x+c)
plt.ylabel("V (V)")
plt.xlabel("f (Hz)")
plt.title("Millikan's Photoelectric Effect Experiment")
error = 100* (np.abs(m*sci.e)-sci.h)/sci.h
print("Planks Constant: ",m*sci.e)
print("Error: ",error,"%")
plt.show()
print(m,c)