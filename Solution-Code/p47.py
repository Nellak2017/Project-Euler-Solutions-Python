# Euler 47 
# Aug 31 2018
'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''
def number_prime_factors(number):
    # Returns number of prime factors of number
    i = 2
    a = set()
    while i < number**.5 or number == 1:
        if number % i == 0: 
            number /= i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)

def main():
    j = 2*3*5*7
    while True:
        if number_prime_factors(j) == 4:
            j += 1
            if number_prime_factors(j) == 4:
                j += 1
                if number_prime_factors(j) == 4:
                    j += 1
                    if number_prime_factors(j) == 4:
                        print(j - 3)
                        break
        j += 1
main()