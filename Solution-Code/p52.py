#Euler 52
#Sep 23 2018

'''
Find the Smallest positive integer, x , such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Each iteration, we'll have:
x,2x,3x,4x,5x,6x

if set(x) == set(2x) and set(3x) == set(4x) and ... set(5x) == set(6x):
    return x
Too easy. Running in O(n) time boi
'''
def f(y):
    for x in range(10,y):
    #Limit it to only 10 million rn
        one = set(list(map(int,(str(x)))))
        two = set(list(map(int,(str(2*x)))))
        tre = set(list(map(int,(str(3*x)))))
        fou = set(list(map(int,(str(4*x)))))
        fiv = set(list(map(int,(str(5*x)))))
        six = set(list(map(int,(str(6*x)))))
        if one == two and two == tre and tre == fou and fou == fiv and fiv == six:
            return x

print(f(10**7))
# This was one of the easiest project Euler problems to solve lol