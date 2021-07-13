# Euler 34
# Aug 28 2018

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''
def findFact():
    facts = [1,1,2,6,24,120,720,5040,40320,362880]
    limit = 362880 * 9
    ans = -3 # Note: As 1! = 1 and 2! = 2 are not sums they are not included.
    for i in range(0,limit):
        total = 0
        stringI = str(i)
        for j in stringI:
            total += facts[int(j)]
        if total == i:
            ans += i
    return ans

#findFact()
print(findFact())