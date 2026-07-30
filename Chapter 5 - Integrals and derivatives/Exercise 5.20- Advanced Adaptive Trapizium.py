import numpy as np 
import matplotlib.pyplot as plt
accuracy = 1e-4


def f(x):
    if x==0:
        return 1
    return (np.sin(x)**2)/(x**2)

def step(x1,x2,f1,f2):
    h = (x2-x1)/1
    I1= h*(f1+f2)/2
    h = (x2-x1)/2
    I2 = h*(f1+f2)/2 + h*f(x1+h)
    error = (I2-I1)/3
    if abs(error) <= accuracy:
        plt.scatter([x1,x2],[f1,f2])
        return I2
    else:
        split = (x2-x1)/2
        xnew = x1+split
        return step(x1,xnew,f1,f(xnew)) + step(xnew,x2,f(xnew),f2)


print(step(0,10,f(0),f(10)))
#1.518619613012486
xls = np.linspace(0,10,1000)
fls =[f(x) for x in xls]
plt.plot(xls,fls)
plt.show()
