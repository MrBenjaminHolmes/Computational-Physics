def factorial(x):
    fac = 1.0
    for n in range(1,x+1):
        fac*=n
    return float(fac)


print(factorial(200))

#Integer Output of 200! : 788657867364790503552363213932...
#Floating Point Output of 200!: inf