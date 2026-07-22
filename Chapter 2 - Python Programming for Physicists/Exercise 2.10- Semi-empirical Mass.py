A = int(input("Enter Mass Number (A): "))
Z = int(input("Enter Atomic Number (Z): "))

a1 = 15.8e6
a2 = 18.3e6
a3 = 0.714e6
a4 = 23.2e6

if A % 2 != 0:
    a5 = 0
elif Z % 2 == 0:
    a5 = 12e6
else:
    a5 = -12e6

B = (a1 * A) \
    - (a2 * (A ** (2 / 3))) \
    - (a3 * ((Z ** 2) / (A ** (1 / 3)))) \
    - (a4 * (((A - (2 * Z)) ** 2) / A)) \
    + (a5 / (A ** 0.5))

print("Binding Energy:", B / 1e6, "MeV")
print("Binding Energy per Nucleon:", (B / 1e6) / A, "MeV")

#Enter Mass Number (A): 58
#Enter Atomic Number (Z): 28
#Binding Energy: 497.5620206224375 MeV
#Binding Energy per Nucleon: 8.57865552797306 MeV