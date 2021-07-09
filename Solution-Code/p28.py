# Euler 28
# Aug 26 2018
# Number spiral diagonals
# Diagonal sums in a 1001 * 1001 spiral ?
'''
21 22 23 24 25
20 7  8  9  10
19 6  1  2  11
18 5  4  3  12
17 16 15 14 13

Diagonal sums = 101

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20 7  8  9  10 27
40 19 6  1  2  11 28
39 18 5  4  3  12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

=
43               7^2
   21          5^2
      7     3^2
         1
      2^2+1 3
   4^2+1      13
6^2+1           31

The below start at x = 1, with the exception of the last, starting at x = 0

UL: 4x^2 - 6x + 3
UR: 4x^2 - 4x + 1
BL: 4x^2 - 8x + 5
BR: 4x^2 - 10x + 7

The summation formulas for each:

UL: 1/3 n (4n^2 - 3n + 2)
UR: 1/3 n (4n^2 -      1)
BL: 1/3 n (4n^2 - 6n + 5)
BR: 1/3 n (4n^2 - 9n + 8)


Test:
   1  2   3   4   5
UL:1  8   29  72  145
UR:1  10  35  84  165
BL:1  6   23  60  125
BR:1  4   17  48  105

 S:1  25  101 261 537 ... = 1/3 (16n^3 - 18n^2 + 14n - 9)
# Note, I subtract 3 every time, because it is counted 3 extra times

The relation between n and the side lengths is simple:

side length = 2n-1

for our problem, it asks for when side length = 1001

1001 = 2n-1
1002 = 2n
501 = n

Finally, the moment you have been waiting for...

1/3 (16n^3 - 18n^2 + 14n - 9), n = 501
=
669,171,001

'''
print(669171001)
