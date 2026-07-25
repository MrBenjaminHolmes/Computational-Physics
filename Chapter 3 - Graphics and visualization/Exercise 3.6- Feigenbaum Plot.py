import matplotlib.pyplot as plt

r_values = []
x_values = []

r = 1.0

while r <= 4.0:
    x = 0.5

    for _ in range(1000):
        x = r * x * (1 - x)

    for _ in range(1000):
        x = r * x * (1 - x)
        r_values.append(r)
        x_values.append(x)

    r += 0.01

plt.scatter(r_values, x_values, s=0.5, color="red")
plt.xlabel("r")
plt.ylabel("x")
plt.title("Feigenbaum (Bifurcation) Diagram")
plt.show()