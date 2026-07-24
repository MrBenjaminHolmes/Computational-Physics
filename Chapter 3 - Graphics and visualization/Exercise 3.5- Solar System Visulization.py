
from vpython import sphere, vector, color, rate
import numpy as np

# Scale factors
distance_scale = 1  
timeFactor= 2e2      
radius_scale = 0.002      

# Sun
sun = sphere(pos=vector(0,0,0),
             radius=69550*0.0005,
             color=color.yellow)

# Planets
mercury = sphere(radius=2440*radius_scale, color=color.gray(0.5))
venus   = sphere(radius=6052*radius_scale, color=color.orange)
earth   = sphere(radius=6371*radius_scale, color=color.blue)
mars    = sphere(radius=3386*radius_scale, color=color.red)
jupiter = sphere(radius=69173*radius_scale, color=color.orange)
saturn  = sphere(radius=57316*radius_scale, color=color.yellow)
theta = 0
while True:
    rate(1*timeFactor)

    mercury.pos = vector(57.9*np.cos(theta/88),      57.9*np.sin(theta/88),      0)
    venus.pos   = vector(108.2*np.cos(theta/224.7),  108.2*np.sin(theta/224.7),  0)
    earth.pos   = vector(149.6*np.cos(theta/365.3),  149.6*np.sin(theta/365.3),  0)
    mars.pos    = vector(227.9*np.cos(theta/687),    227.9*np.sin(theta/687),    0)
    jupiter.pos = vector(778.5*np.cos(theta/4331.6), 778.5*np.sin(theta/4331.6), 0)
    saturn.pos  = vector(1433.4*np.cos(theta/10759.2),1433.4*np.sin(theta/10759.2),0)
    theta += 1