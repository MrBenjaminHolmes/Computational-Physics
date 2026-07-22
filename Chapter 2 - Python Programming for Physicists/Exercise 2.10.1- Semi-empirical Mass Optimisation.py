Z = int(input("Enter Atomic Number (Z): "))
A=Z

a1 = 15.8e6
a2 = 18.3e6
a3 = 0.714e6
a4 = 23.2e6

stable= 0
stableA = 0

while A<=(3*Z):
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

    perNucleon = B/A
    if perNucleon > stable:
        stable=perNucleon
        stableA=A
    A+=1

print("Most Stable Mass Number (A)",stableA)
print("Binding Energy (Mev):",stable / 1e6)

#Enter Atomic Number (Z): 94
#Most Stable Mass Number (A) 230
#Binding Energy (Mev): 7.56603583052652