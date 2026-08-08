import numpy as np 
import scipy.constants as sciconst

#---Constants---#
G =sciconst.G
M = 5.974e24
m = 7.348e22
R = 3.844e8
w = 2.662e-6

accuracy = 1e-6

def f(r):
    return ((w**2)*(r**5)) - (2*(w**2)*R*(r**4)) + ((w**2)*(R**2)*(r**3)) - (G*(M-m)*(r**2)) + 2*G*M*R*r - (G*M*(R**2))

def ddr(r):
    return 5*(w**2)*(r**4) - 8*(w**2)*R*(r**3) + 3*(w**2)*(R**2)*(r**2) - 2*G*(M-m)*r + 2*G*M*R

x= R/2
delta = 1
while abs(delta)>accuracy:
    delta = (f(x))/(ddr(x))  
    x-= delta

print("r = ",x,"m")