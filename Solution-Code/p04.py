#Project Euler Problem 4
#Find the largest Palindrome made from the product of two 3-digit numbers

def is_palindrome(s):
  digits = list(str(s))
  return digits[::-1] == digits[:]
  
def main():
  product = 1
  for i in range(100,999):
    for x in range(100,999):
      if is_palindrome(i*x) and (i*x) > product:
        product = i*x
  return product

print(main())
'''
Simply search through all the 3 digit numbers to determine which 2 produce the maximum Palindrome product.
'''
