import numpy as np
import matplotlib.pyplot as plt
N = 100000
area = [ ]

def f(x):
    return np.exp(-x**2)

for n in range(31):
    h = n/N

    I =f(n)+f(0)

    for i in range(1,N,2):
        I += 4 * f(n - i*h)

    for i in range(2,N,2):
        I += 2 * f(n - i*h)

    I *= h/3

    print("x =", n, ", I =", I)
    area.append(I)

x = np.arange(31)
plt.plot(x,area)
plt.hlines(np.sqrt(np.pi)/2,0,30,linestyle=':',color="red")
plt.show()

#x = 0 , I = 0.0
#x = 1 , I = 0.7468241328124333
#x = 2 , I = 0.8820813907624163
#x = 3 , I = 0.8862073482595184
#......
#x = 25 , I = 0.8862269254527511
#x = 26 , I = 0.8862269254527476
#x = 27 , I = 0.8862269254527531
#x = 28 , I = 0.8862269254527483
#x = 29 , I = 0.8862269254527498
#x = 30 , I = 0.8862269254527514