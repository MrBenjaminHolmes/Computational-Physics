import numpy as np

A = np.array([
    [2, 1, 4, 1],
    [3, 4, -1, -1],
    [1, -4, 1, 5],
    [2, -2, 1, 3]
], float)


v = np.array([-4,3,9,7],float)
N= len(v)
L = np.identity(N,float)
U= A.copy()



for m in range(N):

    for i in range(m+1,N):
        factor = U[i,m]/ U[m,m]
        L[i,m] = factor
        U[i,:] -= factor*U[m,:]




#Forward Sub
y=np.zeros(N,float)
for i in range(N):
    y[i] = v[i]-np.dot(L[i,:i],y[:i])

#Backsub
x=np.empty(N,float)
for i in range(N-1,-1,-1):
    x[i] = (y[i]- np.dot(U[i,i+1:], x[i+1:]))/U[i,i]

print(x)


print("L =")
print(L)

print("\nU =")
print(U)
