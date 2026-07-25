import numpy as np 

def quadratic(a,b,c):
    x1 = (-b+np.sqrt((b*b)-(4*a*c)))/(2*a)
    x2 = (-b-np.sqrt((b*b)-(4*a*c)))/(2*a)
    return float(x1),float(x2)

def quadratic2(a,b,c):
    x1 = (2*c)/(-b-np.sqrt((b*b)-(4*a*c)))
    x2 = (2*c)/(-b+np.sqrt((b*b)-(4*a*c)))
    return float(x1),float(x2)

def quadraticIdeal(a,b,c):
    x1 = (-b+np.sqrt((b*b)-(4*a*c)))/(2*a)
    x2 = (2*c)/(-b+np.sqrt((b*b)-(4*a*c)))
    return float(x1),float(x2)

print(quadraticIdeal(0.001,1000,0.001))