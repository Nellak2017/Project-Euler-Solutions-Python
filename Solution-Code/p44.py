# Euler 44
# Aug 31 2018
import math
'''
P_n = n(3n-1)/2
P_n^-1 = 1/6(1 + sqrt(24n + 1))
 n is pentagon iff 1+24n is a square and sqrt(1+24n)%6 == 0

find:

P_j+P_k = P_n
P_j-P_k = P_r

D = |P_k - P_j| is minimized

k = 2167 , j = 1020
'''
def isPentagonal(n):
    return (math.sqrt(1+24*n)+1)%6==0 and math.sqrt(1+24*n)-int(math.sqrt(1+24*n))==0

def main():
    result = 0
    notFound = True
    i = 1

    while(notFound):
        i += 1
        n = i * (3 * i - 1) / 2

        for j in range(i-1,0,-1):
            m = j * (3 * j - 1) / 2
            if isPentagonal(n - m) and isPentagonal(n + m):
                result = n-m
                notFound = False
                break
    return result


print(main())
