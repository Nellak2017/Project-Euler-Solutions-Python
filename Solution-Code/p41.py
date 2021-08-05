# Euler 41
# Aug 30 2018
# It took 15 minutes to solve it, looking up how to use reduce and itertools
import Euler_Lib as foo
import itertools
from functools import reduce
# Find the largest pandigital prime, using only 1 copy of its digits
'''
A number is divisible by 3 if the sum of it's digits is divisible by 3
So for this problem, we can safely eliminate pandigital primes that
would be
{2,3,5,6,8,9} digits long

Looking at the primes from the largest to the smallest, we can find the
answer very fast.

'''
for p in itertools.permutations(range(7,0,-1)):
    s = reduce(lambda b, a : 10 * b + a, p)
    if foo.isprime(s):
        print(s)
        break