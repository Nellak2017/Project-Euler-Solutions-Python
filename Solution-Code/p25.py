# Euler 25
# First term in the Fibonnacci sequence that has 1000 digits
import Euler_Lib as f

x = 0
ans = 0
while len(list(str(f.fib(x)))) < 1000:
    ans = f.fib(x)
    x += 1
print(x)