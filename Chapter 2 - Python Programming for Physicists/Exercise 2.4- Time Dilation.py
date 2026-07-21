import numpy as np
import scipy.constants as sci
x = float(input("Enter distance x (light years) : ")) * sci.c
v = float(input("Enter speed v as a fraction of c : ")) * sci.c
t_earth = x/v
lorentzFactor = (1)/(np.sqrt(1-((v**2)/(sci.c**2))))

print("Observer Time: ", t_earth, "years" )
print("Ship Time: ", t_earth/lorentzFactor, "years" )

#Enter distance x (light years) : 10
#Enter speed v as a fraction of c : 0.99
#Observer Time:  10.1010101010101 years
#Ship Time:  1.4249228262288742 years