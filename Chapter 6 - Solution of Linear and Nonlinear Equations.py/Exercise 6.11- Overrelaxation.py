import numpy as np 

c=2
accuracy = 1e-6

def f(x):
    return 1-np.exp(-c*x)

def ddx(x):
    return c*np.exp(-c*x)
#----Regular Relaxation Method----
error = 1e6
x = 1
xvalues = [x]
while (error > accuracy):
    x = f(x)
    xvalues.append(x)
    error = (xvalues[-1]-xvalues[-2])/(1-(1)/(ddx(x)))

print(xvalues[-1])
print("N=",len(xvalues)-1)

#----Over-Relaxation Method----
error = 1e6
x = 1
w= 0.5
xvalues = [x]
while (error > accuracy):
    x = (1+w)*f(x)-w*x
    xvalues.append(x)
    error = abs((xvalues[-1]-xvalues[-2]) / (1 - 1/ddx(x)))

print(xvalues[-1])
print("N=",len(xvalues)-1)