# Euler 48
# Aug 31 2018 

# This problem is trivial in Python
# We want the last 10 digits of the sum(x**x) from 1 to 1000
sum = 0
for x in range(1,1001):
    sum += x**x

print(int("".join(list(map(str, list(map(int,str(sum)))[-10:])))))