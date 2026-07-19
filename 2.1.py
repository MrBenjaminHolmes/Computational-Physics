import numpy as np
while True:
    s = float(input('Enter Tower Height (m):'))
    t = np.sqrt((2*s)/9.81)
    print(t,"s\n")