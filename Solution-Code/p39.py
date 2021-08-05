# Euler 39
# Aug 30 2018
'''
0.) p = 120 -> 3, x > 3, p > 12
1.) if Q is a 3 tuple solution and p = sum(Q), then kp, where k is an
    int, will have atleast that solution.
    From 0 we have: 12n,120n,30n
2.) The candidate number has these properties:
- It is highly divisible
- It is even
- It is relatively large
'''
import Euler_Lib as foo

f = []
for x in range(0,1001):
    a = len(list(foo.divisors(x)))
    f.append(a)
print(f.index(max(f)))

'''
The most highly divisible number in the range of 1 to 1000 is 840.
840 satisfies all the properties so it should be the answer. 
'''