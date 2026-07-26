import numpy as np

def f(x):
    return x**4 -2*x+1

def trapeziumRule(a, b, N, f):

    h = (b - a) / N

    total = f(a) + f(b)

    for i in range(1, N):
        x = a + i * h
        total += 2 * f(x)

    integral = (h / 2) * total
    return integral

print("Approximate integral =", trapeziumRule(0,2,10, f))
print("e2 = ", 1/3*(trapeziumRule(0,2,10,f)-trapeziumRule(0,2,20,f)))

#Approximate integral = 4.50656
#e2 =  0.026633333333333137