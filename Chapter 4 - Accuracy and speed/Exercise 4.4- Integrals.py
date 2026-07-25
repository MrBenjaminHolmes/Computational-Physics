import numpy as np
import time
start_time = time.time()
N= 1212641
h=2/N
I=0

for k in range(N):
    xk=-1+h*k
    I+= h*(np.sqrt(1-xk**2))

print("N=",N,", I=",I)
print("--- %s seconds ---" % (time.time() - start_time))
error = 100* (np.abs(I)-np.pi/2)/np.pi/2
print("Error: ", error,"%")
#N= 1212641 , I= 1.5707963255495843
#--- 1.0132715702056885 seconds ---
#Error:  -1.9819760787626455e-08 %