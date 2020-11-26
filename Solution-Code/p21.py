# Project Euler Problem 21
# Amicable numbers

import Euler_Lib as E

def d(n):
    return sum(E.proper_divisors(n))

def amicable_pairs(start,end):
    pairs = []
    for x in range(start,end):
        if E.is_amicable(x):
            pairs.append(x)
    return pairs

print(sum(amicable_pairs(1,10000)))