import numpy as np

A = np.array([
    [1,4,8,4],
    [4,2,3,7],
    [8,3,6,9],
    [4,7,9,2]
])

N= len(A)

def qr_decomposition(A):
    
    Q = np.zeros((N,N))
    R = np.zeros((N,N))
    a = []
    for i in range(len(A)):
        a.append(A[:, i])

    def q(i):
        return u(i)/np.linalg.norm(u(i))

    def u(i):
        if i ==0:
            return a[0]
        else:
            total = 0
            for j in range(0,i):
                total += (np.dot(q(j),a[i]))*q(j)
            return a[i] - total 

    for i in range (N):
        for j in range(N):
            Q[j][i] = q(i)[j]

    for i in range(N):
        for j in range(i, N):  
            if i == j:
                R[i][j] = np.linalg.norm(u(i))
            else:
                R[i][j] = np.dot(q(i), a[j])
    return Q,R

V = np.identity(N)
tol = 1e-6 
max_iter = 1000
for k in range(max_iter):
    Q,R  = qr_decomposition(A)
    A = R @ Q
    V = V @ Q
    off = A - np.diag(np.diag(A)) 
    error = np.max(np.abs(off))
    if error < tol: 
        break

print("Iterations:", k + 1) 
print("\nEigenvalues:") 
print(np.diag(A)) 
print("\nEigenvectors (columns):") 
print(V) 
print("\nMaximum off-diagonal element:", error)