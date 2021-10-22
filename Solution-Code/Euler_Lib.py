# This file contains all of the library functions used in my project euler solutions
# Keep this file in Alphabetical Order
# Contains:
# digit_sum,esieve,fact,fib,is_palindrome,isprime,maxPF,nth_prime,pf,tri

import math,random

# D

def digit_sum(n):
    result = 0 
    for x in str(n):
        result += int(x)
    return result

# Returns a generator of all the factors of a number
def divisors(n):
    large_divisors = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n/i)
    for divisor in reversed(large_divisors):
        yield int(divisor)

# This function takes numerator n, denominator d and does up to
# p cyles of long division. It stops when either it finds a repeated
# remainder or it has generated a decimal fraction that is has the
# same number of digits as the denominator (The longest possible 
# repeating sequence has length [denominator - 1]).


def divide(n, d, p):
    i = 0  # Counts the cycles
    remainders = set()  # Empty set of remainders

    while i < p:
        if n < d:
            n = n * 10  # If the numerator < denominator, multiply by 10

        n = n % d  # sets the remainder as the new numerator

        if n in remainders:  # If this is repeated remainder, we have reached the end of a repeating cycle
            return (d, i)  # Returns the denominator and the length of the repeating decimal

        else:
            remainders.add(n)  # Adds the new remainder to set of remainders

        i = i + 1  # Increments the counter (number of digits found)
        
    return remainders

# E

def esieve(n):
    # The Sieve of Eratosthenes, O(n) space , O(log log n) time
    # Generates primes up to a limit
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

# F

def fact(n):
    # Returns the factorial of n, where factorial is n*(n-1)*(n-2)...*(1)
    if n >= 0:
        product = 1
        for i in range(n):
            product *= i+1
    else:
        raise ValueError('factorial is not defined for negative numbers')
    return product

def fib(n):
    # Returns fibonnacci(n), where fib(n) = fib(n-1)+fib(n-2)
    a,b = 0,1
    for _ in range(0,n):
        a, b = b, a + b
    return a

# I

def is_amicable(n):
    # Returns true if a number is amicable
    return sum(proper_divisors(sum(proper_divisors(n)))) == n and sum(proper_divisors(n)) != n

def is_palindrome(s):
    # Returns True if a string is a palindrome, False otherwise. 
    # A Palindrome is a string that is the same forwards and backwards.
    digits = list(str(s))
    return digits[::-1] == digits[:]

def isprime(n, k=40):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification
    # Contribution goes to Ayrx / miller_rabin.py

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# M

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

# N

def nth_prime(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break
        else:
            prime_list.append(num)
        # don't check even numbers
        num += 2
    # return the last prime number generated
    return prime_list[-1]

# P

def partition(list,target):
    # This gives the partitions of a number, with the partitions supplied
    # Ex: given british currency, partition 200Pence ==> 73682
    if list is not None:
        ways = [1] + [0] * target
        for p in list:
            for j in range(p, target + 1):
                ways[j] += ways[j - p]
        return ways[-1]
    elif list is None:
        list = list(range(1,target))
        ways = [1] + [0] * target
        for p in list:
            for j in range(p, target + 1):
                ways[j] += ways[j - p]
        return ways[-1]

def proper_divisors(n):
    return [x for x in range(1,((n+1)//2)+1) if n % x == 0]

def pf(n): 
    # Returns the prime factor list of a number
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors 

# S

def sieve(limit):
    # Generates primes up to a limit, as a generator
    a = [True] * limit
    a[0] = a[1] = False
    for (i,isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

# T

def tri(n):
    # Triangle numbers, O(1) time , O(1) space
    # Returns the nth triangle number
    return int(((n*(n+1))/2))