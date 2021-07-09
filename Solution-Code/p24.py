#Project Euler Problem 24
#Lexiographic numbers
#find the 1 millionth number in the permutation group for
# {0,1,2,3,4,5,6,7,8,9}, assuming it follows lexiographic ordering
# The answer is: {2,7,8,3,9,1,5,4,6,0}
import math

def fact(n):
    product = 1
    for x in range(1,(n+1)):
        product *= x
    return product

def elem_in_permutation_group(n, x): # I could simplify this, but I like all the variables, it keeps it simple.
    result = list()
    Seg = [x for x in range(0, x)]
    for i in range(x):
        temp = math.floor((n-1) / fact(x - i))*fact(x - i)
        step = fact(x - (i + 1))
        dist_from_n = (n-1) - temp
        steps_to_n = dist_from_n / step
        r = math.floor(steps_to_n)

        result.append(Seg[r])
        Seg.remove(Seg[r])

    return int(''.join(map(str,result)))

print(elem_in_permutation_group(1000000,10)) # note, n <= x!