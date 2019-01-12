#Project Euler problem 2
#Sum of even fib sequence < 4 million
def fib(n): # Iterative implemenation of the fib function, only adding the even fibs
    # runs in O(n^2) time
    a = 0
    b = 1
    r = 2
    while b <= n :
        if b % 2 == 0 :
            a += b

        b,r = r,b+r
    return str(a)


print(fib(4000000))
