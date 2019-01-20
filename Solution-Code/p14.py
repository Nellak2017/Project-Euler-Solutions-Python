# Euler 14
# Aug 25 2018
# Collatz problem, what collatz chain < 10^6 is the longest?
# n -> n/2 if even and n-> 3n+1 if odd

f = int(1e6) # Using the rarely used e notation for large numbers
longest = 0
the_num = 0
for x in range(1,f):
    num = x
    numCop = x
    iterations = 0
    while num != 1:
        iterations += 1
        if num % 2 == 0:# even
            num /= 2
        elif num % 2 != 0:# odd
            num = 3*num + 1
    the_num = numCop if iterations > longest else the_num
    longest = iterations if iterations > longest else longest


print(longest) # Not the answer
print(the_num) # The answer
