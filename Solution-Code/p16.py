# Project Euler Problem 16
# Sum of digits of 2^1000

def sumDigits(n):
    digits = list(str(n))
    sum = 0
    for x in digits:
        sum += int(x)
    return sum

print(sumDigits(2**1000)) 
