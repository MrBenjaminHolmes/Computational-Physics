import numpy as np
import scipy.constants as sci
while True:
    s = float(input('Enter Tower Height (m):'))
    t = np.sqrt((2*s)/sci.g)
    print("Time Taken: ",t,"s\n")

#Enter Tower Height (m):10
#Time Taken:  1.4280869812290344 s