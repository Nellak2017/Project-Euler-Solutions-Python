# Euler 26
# Aug 26 2018
# Reciprical cycles
# What is the largest recurring cycle in its decimal fraction part for 1/d?
# in the range d < 1000

'''
I could use the brent cycle finding algorithm on each of the numbers less than 1000,
however, that would be hard.
I'd rather use the tortise and hare approach.
'''

# We need to do long division to get enough digits!
'''
This function takes numerator n, denominator d and does up to
p cyles of long division. It stops when either it finds a repeated
remainder or it has generated a decimal fraction that is has the
same number of digits as the denominator (The longest possible 
repeating sequence has length [denominator - 1]).
'''


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

longest = [0, 0]
largest_denominator = 1000
for x in range(2, largest_denominator + 1):
    y = divide(1, x, x)  # p = x due to upper bound on length of repeating decimal (see above)
    if y[1] > longest[1]:
        longest = y

print('1 / %s has longest recurring decimal (length = %s) for denominators less than %s' % (
longest[0], longest[1], largest_denominator))