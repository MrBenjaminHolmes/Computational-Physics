import numpy as np

def f(x):
    return x*(x-1)

x=1
for delta in [1e-4,1e-6,1e-8,1e-10,1e-12,1e-14,1e-15]:
    dfdx = (f(x+delta)-f(x))/delta
    print("δ:",delta,", dfdx=",dfdx)


#dfdx = 1.010000000000001
#In reality dfdx = 1 exactly  
#δ: 0.0001 , dfdx= 1.0000999999998899
#δ: 1e-06 , dfdx= 1.0000009999177333
#δ: 1e-08 , dfdx= 1.0000000039225287
#δ: 1e-10 , dfdx= 1.000000082840371
#δ: 1e-12 , dfdx= 1.0000889005833413
#δ: 1e-14 , dfdx= 0.9992007221626509
#δ: 1e-15 , dfdx= 1.1102230246251577