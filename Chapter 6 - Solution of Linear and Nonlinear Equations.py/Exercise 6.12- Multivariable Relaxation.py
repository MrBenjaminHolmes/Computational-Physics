import numpy as np

a = 1
b = 2

x = 1.0
y = 0.3
print("--------Doesnt Converge--------")
for i in range(20):
    x_new = y * (a + x**2)
    y_new = b / (a + x**2)

    x = x_new
    y = y_new

    print(i, x, y)


x = 1.0
y = 0.3
print("--------Convergance Rearrangement--------")
for i in range(20):
    x = np.sqrt(b/y - a)
    y = x / (a + x**2)

    print(i, x, y)