import numpy as np 
import scipy.constants as sci

def altitude(T):
    h = np.cbrt((sci.G * 5.97e24 * T**2 )/(4*(sci.pi)**2)) - 6371e3
    return h

T = float(input('Enter Orbit Time (s):'))
print("Altitude at T=",T,":",altitude(T),"m\n")


print("Altitude at T=24hrs: ",altitude(24*60*60),"m")
print("Altitude at T=90mins: ",altitude(90*60),"m")
print("Altitude at T=45mins: ",altitude(45*60),"m")
print("Altitude at T=23.93hrs: ",altitude(23.93*60*60),"m")
print("Difference:",altitude(24*60*60)-altitude(23.93*60*60),"m")

#Enter Orbit Time (s):12000
#Altitude at T= 12000.0 : 4956331.313454084 m

#Altitude at T=24hrs:  35864982.475448266 m
#Altitude at T=90mins:  280750.42297603004 m
#Altitude at T=45mins:  -2180659.811722687 m
#Altitude at T=23.93hrs:  35782816.9800006 m
#Difference: 82165.49544766545 m