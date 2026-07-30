import numpy as np 

B = np.array([
    [4,-1,-1,-1],
    [-1,3,0,-1],
    [-1,0,3,-1],
    [-1,-1,-1,4]
],float)

A = np.array([
    [0,1,4,1],
    [3,4,-1,-1],
    [1,-4,1,5],
    [2,-2,1,3]
],float)

v= np.array([-4,3,9,7],float)
N = len(v)

for m in range(N):

    pivot = m + np.argmax(np.abs(A[m:, m]))

    if pivot != m:
        A[[m, pivot]] = A[[pivot, m]]
        v[[m, pivot]] = v[[pivot, m]]

    div = A[m,m]
    A[m,:]/= div
    v[m]/=div

    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

x = np.empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m]-=A[m,i]*x[i]

print(x)
