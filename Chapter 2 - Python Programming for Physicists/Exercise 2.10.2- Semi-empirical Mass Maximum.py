stable= 0
stableA = 0
stableZ = 0
for Z in range(1,101):
    A=Z

    a1 = 15.8e6
    a2 = 18.3e6
    a3 = 0.714e6
    a4 = 23.2e6

    

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
            stableZ=Z
        A+=1

print("Most Stable Mass Number (A)",stableA)
print("Most Stable Atomic Number (Z)",stableZ)
print("Binding Energy (Mev):",stable / 1e6)

#Most Stable Mass Number (A) 62
#Most Stable Atomic Number (Z) 28
#Binding Energy (Mev): 8.70245768367189

