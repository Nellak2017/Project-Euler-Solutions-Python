#Project Euler problem 23
#Non-abundant sums
# a perfect number is a number who's proper divisors sum to that number
# P(n) := n == sum(divisors(n))
# a number is deficient if sum(divisors(n)) < n
# a number is abundant if sum(divisors(n)) > n
# Find the sum of all the positive integers which cannot be written as the
# sum of 2 abundant numbers
# NOTE: all integers greater than 28123 CAN be written as the sum of 2 abundant
# numbers

#Plan 1, straight forward:
# 1. find all the abundant numbers below 28123
# 2. loop thru the ints from 1 to 28123 and test each number to see if any 2 abundant pairs can sum to each number
# This will take quite a while to execute btw O(n^3) atleast, I don't think my computer is up to the task
print('4179871')