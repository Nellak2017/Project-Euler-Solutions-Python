#Euler 51
'''
Observations:
1. The smallest eight prime value family member is greater than 56993
2. The smallest eight prime value family member is not 5 digits or less
3. The smallest eight prime value family member is atleast 6 digits
4. The last digit is in 1,3,7,9
5. The sum of the digits can't be divisible by 3
6. 5 digits in a 6 digit number can't be repeated


XXXXXY -> Disallowed
YXXXXX -> Disallowed

XXXXAB -> ?
XXXAXB -> ?
XXAXXB -> ?
XAXXXB -> ?
AXXXXB -> ?
ABXXXX -> ?

Hmm...

The smallest 6 digit number starts with 1..

1XXXXY

The smallest prime for Y is 3

1XXXX3

So this is a logical first location to begin my search!
Only 9999 possibilities! Right?
No. There are much less than that.
let's start with the smallest and work up!

Repeating 5 digits = 0%
Repeating 4 digits = 12%
Repeating 3 digits = 97.4%
Repeating 2 digits = 99.9%
Repeating 1 digits = 0%

111113 -> impossible

1111x3 -> 12%
...

111xx3 -> 99.08%
...

11xxx3 -> 92%
...

1xxxx3 -> disallowed

Lets begin the search with the repeating 3 of the 1's with a 3 at the end!

111xx3
11x1x3
1x11x3
x111x3 -> exclude this family

A nested for loop shall suffice!

However, lets just brute force it instead, it took my machine a while to generate the result.
'''
import Euler_Lib as E
from itertools import count, dropwhile

ALL_DIGS = '0123456789'
def not_in_family(prime, nfamily = 8):
    ALL_DIGS = '0123456789'

    def not_in_family(prime, nfamily=8):
        sp = list(str(prime));ndig = len(sp)
        for nrepeat in range(1, ndig):
            # for every number of the recurring digit's repeats
            # try first family digit
            for ffd in ALL_DIGS[:-nfamily + 1]:
                if sp[:-1].count(ffd) < nrepeat:
                    continue  # if insufficient number of repeats

                # find indexes in `prime' of `ffd'
                inds = [sp.index(ffd)]
                for i in range(nrepeat - 1):
                    inds.append(sp.index(ffd, inds[i] + 1))

                # find family
                s = sp[:];fam = [prime]
                digs = ALL_DIGS[ALL_DIGS.index(ffd) + 1:]
                nfail, nfailmax = 0, len(digs) - nfamily + 1
                for dig in digs:
                    for i in inds:
                        s[i] = dig  # replace corresponding digits
                    p = int(''.join(s))
                    if E.isprime(p):fam.append(p)
                    elif nfail == nfailmax:break
                    else:nfail += 1

                if len(fam) >= nfamily:
                    for i in inds:  # pretty printing stuff
                        s[i] = '*'
                    print(''.join(s), fam)
                    # `prime' begins a `nfamily' prime value family
                    return False
                    # `prime' does NOT begin the family
        return True

print(list(dropwhile(not_in_family, filter(E.isprime, count(1,1)))))

# result = *2*3*3 [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
# answer is 121313