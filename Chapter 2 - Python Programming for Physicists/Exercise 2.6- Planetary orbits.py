import numpy as np
from astropy import constants as const
import scipy.constants as sci

l1 =float(input("Enter Distance From Sun at Perihelion (m): "))
v1 =float(input("Enter Velocity of Object at Perihelion (m/s): "))
#l1=1.4710e11
#v1=3.0287e4
v2 = ((sci.G*const.M_sun.value)/(l1*v1))-(np.sqrt(((sci.G**2*const.M_sun.value**2)/(l1**2*v1**2))+(v1**2)-((2*sci.G*const.M_sun.value)/(l1))))
l2 = (l1*v1)/v2

a = 0.5*(l1+l2)
b=np.sqrt(l1*l2)
T = (2*sci.pi*a*b)/(l1*v1)
e =(l2-l1)/(l2+l1)

print("Speed at Aphelion (m/s): ",v2)
print("Distance from Sun at Aphelion (m): ",l2)
print("Semi-Major Axis (m): ",a)
print("Semi-Minor Axis (m): ",b)
print("Orbital Period: ",T,"(s) ",T/86400,"(days)")
print("Orbital Eccentricity: ",e)


#--- Halley’s comet ---#
#Enter Distance From Sun at Perihelion (m): 8.7830e10
#Enter Velocity of Object at Perihelion (m/s): 5.4529e4
#Speed at Aphelion (m/s):  891.5987704541221
#Distance from Sun at Aphelion (m):  5371566481143.365
#Semi-Major Axis (m):  2729698240571.6826
#Semi-Minor Axis (m):  686865841368.4741
#Orbital Period:  2459778556.0821157 (s)  28469.659213913375 (days)
#Orbital Eccentricity:  0.9678242822981028


# #--- Earth ---#
#Enter Distance From Sun at Perihelion (m): 1.4710e11
#Enter Velocity of Object at Perihelion (m/s): 3.0287e4
#Speed at Aphelion (m/s):  29289.186366830185
#Distance from Sun at Aphelion (m):  152111350728.59195
#Semi-Major Axis (m):  149605675364.29596
#Semi-Minor Axis (m):  149584690701.20737
#Orbital Period:  31560665.68459151 (s)  365.2854824605499 (days)
#Orbital Eccentricity:  0.016748531485817984