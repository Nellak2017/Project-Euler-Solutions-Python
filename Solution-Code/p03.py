#Project Euler problem 3
#Largest prime factor of 600851475143
import math

def maxPrimeFactor(n):
    
    maxPrime = -1
    
    while n%2 == 0:
        maxPrime = 2
        n /= 2
        
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        while n % x == 0:
            maxPrime = x
            n = n / x
    
    if n > 2:
        maxPrime = n
        
    return int(maxPrime)

print(maxPrimeFactor(600851475143))
