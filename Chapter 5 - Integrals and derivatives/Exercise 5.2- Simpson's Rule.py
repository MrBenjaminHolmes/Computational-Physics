import numpy as np

a=2
b=0
N=100000
h=(b-a)/N

def f(x):
    return x**4 - 2*x +1

I= (f(a)+f(b))

for i in range(1,N-1,2):
    I+= 4* f(a+i*h)
for i in range(2,N,2):
    I+= 2* f(a+i*h)

I*=(1/3)*h
error = 100* (np.abs(I)-4.4)/4.4
print("N=",N, ", I=",abs(I), ", Error (%) =",error)

#N= 100 , I= 4.374400038399999 , Error (%) = -0.5818173090909342
#N= 1000 , I= 4.397344000004228 , Error (%) = -0.06036363626755142
#N= 10000 , I= 4.399733440000019 , Error (%) = -0.0060581818177585225
#N= 100000 , I= 4.399973334400009 , Error (%) = -0.0006060363634364694
#Actual Value = 4.4