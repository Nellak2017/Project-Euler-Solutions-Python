#Project Euler Problem 6
#Difference between sum of squares and squares of sums
#Formula: (n(n+1)(2n+1))/6 - (n(n+1)/2)^2
n = 100
print(int((n*(n+1)/2)**2 - (n*(n+1)*((2*n)+1))/6))
'''
For this problem, all that needs to be done is a simple google search for the sum of squares formula.
Take the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum, and you have it.
'''
