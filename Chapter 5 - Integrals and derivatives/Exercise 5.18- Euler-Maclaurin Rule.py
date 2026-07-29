import numpy as np 

def f(x):
    return x**4 -2*x+1

def EulerMaclaurin(a, b, N, f):

    h = (b - a) / N

    total = f(a) + f(b)

    for i in range(1, N):
        x = a + i * h
        total += 2 * f(x)

    integral = (h / 2) * total

    fad= ((f(a+h/2))-(f(a-h/2)))/h
    fbd = ((f(b+h/2))-(f(b-h/2)))/h

    integral += (h**2)/12 * (fad -fbd)
    
    return integral

N=10
I=EulerMaclaurin(0, 2, N, f)
error = 100* (np.abs(I)-4.4)/4.4
print("N=",N, ", I=",abs(I), ", Error (%) =",error)

#N= 10 , I= 4.399626666666667 , Error (%) = -0.008484848484843512