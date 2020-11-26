#Project Euler Problem 10
#Sum of primes less than 2 million
import Euler_Lib as E

def primes_Sum(n):
    sum = 0
    for x in range(2,n+1):
        if(E.isprime(x)):
            sum += x
    return sum

print(primes_Sum(2000000))