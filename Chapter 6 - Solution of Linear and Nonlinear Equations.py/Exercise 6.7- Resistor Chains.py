import numpy as np
N = 6
v_plus = 5

v = np.zeros(N, int)
v[:2] = v_plus

A = np.zeros((N, N), dtype=int)
for i in range(N):
    if i==0 or i==N-1:
        A[i,i]=3
    else:
        A[i,i]=4

    if i - 1 >= 0:

        A[i, i - 1] = -1

    if i - 2 >= 0:
        A[i, i - 2] = -1

    if i + 1 < N:
        A[i, i + 1] = -1

    if i + 2 < N:
        A[i, i + 2] = -1

print("A:",A)
print("v:",v)
x = np.linalg.solve(A,v)

print(x)