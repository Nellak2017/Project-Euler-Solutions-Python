#Project Euler Problem 5
#Smallest positive number that n%2 to n%20 == 0
import math
from Solution-Code import Euler_Lib as E

def primesProduct(n):
  product = 1
  for x in range(2,n+1):
    if(E.isprime(x)):
      product *= x
  return product

def optimized(a,b):
  # for the number to be a candidate, it will need to be divisible by all the primes less than
  # b. Using this fact, one could search this space from that prime product up to b! at prime_Product intervals
  # This reduces the search space from atleast b! to only (b!-primesProduct)/primesProduct(b)
  theNum = E.fact(b)
  for x in range(primesProduct(b),E.fact(b),primesProduct(b)):
      # starting at b and counting to fact(b) by the product of primes less than b
      for i in range(b,a,-1):# if it's not a candidate, prune it fast
          if(x%i != 0):
              break
          elif(i==2): # if it reaches this stage, it's worthy to be printed
              return x if x<theNum else theNum

print(optimized(1,20))  
