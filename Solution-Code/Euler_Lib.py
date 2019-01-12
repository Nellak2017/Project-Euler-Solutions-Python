#This file contains all of the library functions used in my project euler solutions
#Keep this file in Alphabetical Order
#Contains:
#fib,maxPF

import math

def fib(n):
    # Returns fibonnacci(n), where fib(n) = fib(n-1)+fib(n-2)
    a,b = 0,1
    for x in range(0,n):
        a, b = b, a + b
    return a

def is_palindrome(s):
    # Returns True if a string is a palindrome, False otherwise. 
    # A Palindrome is a string that is the same forwards and backwards.
    digits = list(str(s))
    return digits[::-1] == digits[:]

def maxPF(n):
    # Returns the max prime factor of a number
    maxPrime = -1
    while n%2 == 0:
        maxPrime = 2
        n /= 2
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        while n % x == 0:
            maxPrime = x
            n = n / x
    if n > 2:
        maxPrime = n    
    return int(maxPrime)    
    
