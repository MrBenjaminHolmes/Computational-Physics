import numpy as np
x = 1  # C0
n = 0

while x <= 1e9:
    print(f"C{n} = {int(x)}")
    n += 1
    x *= (4*n - 2) / (n + 1)