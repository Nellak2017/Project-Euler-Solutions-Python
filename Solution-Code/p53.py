#Euler 53
#Sep 26 2018
'''
How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

n C r = n! / (r!*(n-r)!)
Idea 1:
for i in range 23 to 100
 for j in range
'''
def fact(n):
    product = 1
    for i in range(n):
        product *= i+1
    return product

def choose(n,r):
    # n choose r = n! / (r!*(n-r)!)
    return int(fact(n) / (fact(r) * fact(n - r)))

def main():
    li = list(range(1,101))
    sum = 0
    for i in range(23,101):
        for j in range(2,li[i-1]):
            # Each iteration, the j can increase by 1
            if choose(i,j) > 10**6:
                sum += 1
    return sum

print(main())

