from scipy.integrate import quad

def f(x):
    return x**4 - 2*x + 1

a = 0.0
b = 2.0

s, error = quad(f, a,b)

print(f"{s:.1f}")