import numpy as np
import scipy.constants as sci

E = 10 * sci.electron_volt
V = 9 * sci.electron_volt

k1 = (np.sqrt(2*sci.electron_mass*E))/(sci.hbar)
k2 = (np.sqrt(2*sci.electron_mass*(E-V)))/(sci.hbar)

T= (4*k1*k2)/((k1+k2)**2)
R= ((k1-k2)/(k1+k2))**2

print("Probability of Transmission: ",T)
print("Probability of Reflection: ",R)
print("Total Probability: ", T+R)

#Probability of Transmission:  0.7301261363877617
#Probability of Reflection:  0.26987386361223825
#Total Probability:  1.0