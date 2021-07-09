# Euler 32
# Aug 28 2018

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

ran = range(0,10)
possa = [10*a + b for a in ran for b in ran if a < b or a > b ]
possb = []
for a in range(100,9999):
    x = str(a)
    y = set(x)
    if len(x) == len(y): possb.append(a)
sol = []
for a in possa:
    for b in possb:
        if b < max(a,1000.0 / a): continue
        if b > 9999.0 / a: break
        c = a*b
        if "".join(sorted(str(a)+str(b)+str(c))) == "123456789":
            sol.append(c)
sol = set(sol)
print(sum(sol))