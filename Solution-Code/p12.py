# Project Euler Problem 12
# first triangle num to have over 500 divisors, where a triangle num, T(n) = (n*(n+1))/2
import Euler_Lib as E

def test(n):
  # We use this function to test each n if it has atleast 500 factors in the compute function
  a = E.pf(n)
  exp_list_plus_1 = list()
  
  for x in set(E.pf(n)):
    # Note, we are counting how many times each element is repeated
    exp_list_plus_1.append(a.count(x)+1)
  product = 1
  
  for x in exp_list_plus_1:
    product *= x
  return product

def compute():
  a = list() # We have to make a list of the 845 candidates to search through, based on the math as explained below
  for i in range(11764,12609):
    a.append((i*(i+1))/2) # Using the triangle number formula
  for x in a:
    # We now have to search through the candidates to find the value I want
    if(test(x) > 500):
      return x

print(compute())

'''
MATH:

The formula for a given triangle number is given by n(n+1)/2
Factoring gives (n/2+1/2)*n/2
if n is even n+1, n/2
if n is odd 1/2(n+1),n

I will exploit the fact that Product(Prime_Factor_i's exponent + 1) = num factors
Ex: 36 = 3^2*2^2 => (2+1)*(2+1) => 3*3 = num factors = 9

Since the problem states that the number has 500 divisors, we can eliminate all the numbers below that.
500 = n(n+1)/2 ; n ~ 32
therefore, n > 32

We also know that when n = 32, it's factors are as follows:

33,16 -> (2^5 - 1 , 2^4) -> ((3*11),2^4) -> (3,11,2^4)

Every time I double this, I will get closer to The number I want exponentially fast

2(3*11),2^5 ; 4(3*11),2^6 ; ...

The number of factors in these are as follows:

2^n(4),2^(n+3) => (n+1)*(n+3)*(4) = (4n^2+16n+12)

Knowing it needs to be atleast 500:

500 = 4n^2+16n+12 => n ~ 9 # rounded down

Plugging in 9 into the values:

2^9*(11*3)*2^(12) = 69206016

We now know 69206016 < n(n+1)/2 < 79496836 

And that 11764 < n < 12609

We have narrowed our search space considerably to only 845 candidates, as opposed to 12609 (15 times speed up)

'''
