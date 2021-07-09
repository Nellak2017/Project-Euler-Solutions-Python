# Euler 27
# Aug 26 2018
# n^2 + n + 41 -> 40 primes for consecutive natural nums 0 <= n <= 39
# n^2 + an + b, where |a| < 1000 and |b| <= 1000
# find a*b for the quadratic that produces the max number of primes for
# consecutive values of n, starting at n = 0
'''
The formula n^2-79n+1601 is nothing more than (n-40)^2+n-40+41
so that all the forty primes of n^2+n+41 are met twice that's why 80 primes are found, but only 40 different ones.
So what I did was:
take (n-p)^2+n-p+41, working out this formula gives:
n^2-(2p-1)n+p^2-p+41.
Now |2p-1|<1000 and |p^2-p+41|<1000.
The second condition gives -30<=p<=31
The value p=31 gives the most primes.
So the numbers are -(2*31-1)=-61 and 31^2-31+41=971.
See also: http://mathworld.wolfram.com/Prime-GeneratingPolynomial.html
'''
print(-61 * 971)