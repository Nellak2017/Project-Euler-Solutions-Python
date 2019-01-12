#Project Euler problem 9
#pythagorean triple that sums to 1000
'''
SOME MATH
Observing that squaring any imaginary number yields
an integer pythagorean triplet, and using this fact to
generalize, I found a formula for generating pythagorean triples.
it is: (u^2-v^2,2uv,u^2+v^2)
summing those variables and setting it equal to 1000 yields
24 unique solutions
the problem asked for natural number solutions, so instead of
looking through a space of 1000^3, I simplified it to only
24 using high school math.(This is a 43.66 million times speed up)
searching these numbers yields:
u = -20, v = -5
which results in (375,200,425)
'''
u = -20
v = -5

print("(",(2*u*v),",",(u**2 - v**2),",",(u**2 + v**2),")")
print("Sum = ",(u**2 - v**2)+(u**2 + v**2)+(2*u*v))
print("Product = Answer = ",(u**2 - v**2)*(u**2 + v**2)*(2*u*v) )
