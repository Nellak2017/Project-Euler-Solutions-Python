# Euler 50
# Aug 31 2018
import Euler_Lib as E

primes = list(E.sieve(10**6))
length = 0
largest = 0
lastj = len(primes)

for i in range(len(primes)):
    for j in range(i+length,lastj):
        sol = sum(primes[i:j])
        if sol < 10**6:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break
print(largest)
