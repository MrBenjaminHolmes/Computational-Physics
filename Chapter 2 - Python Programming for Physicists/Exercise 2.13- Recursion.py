def catNum(n): 
    if n == 0: 
        return 1
    return ((4*(n-1)+2)/((n-1)+2))*catNum(n-1) 

print(catNum(100))

def GCD(m,n):
    if n == 0: 
        return m
    return GCD(n,(m%n))

print(GCD(108,192))