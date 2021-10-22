# Euler 49
# Aug 31 2018

import Euler_Lib as E
from itertools import permutations

def create(b):
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            difference = b[j] - b[i]
            if b[j] + difference in b:
                return str(b[i])+str(b[j])+str(b[j]+difference)
    return False

primes = E.sieve(10000)

primes = [x for x in primes if x > 1487]

for i in primes:
    p = permutations(str(i))
    a = [int(''.join(x)) for x in p]
    a = list(set([x for x in a if x in primes]))
    a.sort()
    if len(a) >= 3:
        if create(a):
            print(create(a))
            break