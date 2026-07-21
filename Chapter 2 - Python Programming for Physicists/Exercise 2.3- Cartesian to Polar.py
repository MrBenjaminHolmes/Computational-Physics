import numpy as np 
import scipy.constants as sci
x= float(input("X:"))
y= float(input("Y:"))

r = np.sqrt((x)**2+(y)**2)
theta = np.arctan2(y,x) *(180/(sci.pi))

print("r:",r,", θ:",theta,"deg")

#X:10
#Y:4
#r: 10.770329614269007 , θ: 21.80140948635181 deg