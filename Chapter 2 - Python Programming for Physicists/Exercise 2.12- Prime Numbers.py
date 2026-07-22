primes = [2]

for i in range(3,10001):
    is_prime = True

    for prime in primes:
        if prime * prime > i:
            break
        if(i%prime == 0):
            is_prime = False
        
    if is_prime == True:
        primes.append(i)

print(primes)
print(len(primes))



