import numpy as np 

A = np.array([
    [4,-1,-1,-1],
    [-1,3,0,-1],
    [-1,0,3,-1],
    [-1,-1,-1,4]
],float)

v= np.array([5,0,5,0],float)

print(np.linalg.solve(A,v))