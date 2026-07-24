from vpython import sphere , vector , color
import numpy as np
L=5
R=0.3
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if (i+j+k)%2 ==0 :
                sphere(pos=vector(i,j,k),radius=R, color = color.red)
            else:
                sphere(pos=vector(i,j,k),radius=R, color = color.blue)

while True:
    continue