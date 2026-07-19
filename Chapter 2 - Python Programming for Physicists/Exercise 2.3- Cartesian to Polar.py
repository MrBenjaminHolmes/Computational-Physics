import numpy as np 
import scipy.constants as sci
x= float(input("x:"))
y= float(input("y:"))

r = np.sqrt((x)**2+(y)**2)
theta = np.arctan2(y,x) *(180/(sci.pi))

print(r,",",theta,"deg")