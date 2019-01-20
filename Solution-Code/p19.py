# Project Euler 19
# Aug 25 2018
# How many Sundays fell on the first of the month during the 20th century?
# (1 Jan 1901 to 31 Dec 2000)
# Using simple reasoning to solve the puzzle
'''
days in the months:
JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC
31  28  31  30  31  30  31  31  30  31  30  31
    29
     JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC | SUM
1901:TUE FRI FRI MON WED SEP MON THU SUN TUE FRI SUN | 2
.
.
1904:FRI MON TUE

RULES:
28 -> 31 = +0 days
29 -> 31 = +1 days
30 -> 31 = +2 days
else     = +3 days

Mon Tue Wed Thu Fri Sat Sun
0   1   2   3   4   5   6

leap:    +3  +1
      +3 +3  +0  +3  +2  +3  +2  +3  +3  +2  +3  +2
     JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC | SUM
1901:1   4   4   0   2   5   0   3   6   1   4   6   | 2
1902:2   5   5   1   3   6   1   4   0   2   5   0   | 1
1903:3   6   6   2   4   0   2   5   1   3   6   1   | 3
1904:4   0   1   4   6   2   4   0   3   5   1   3   | 1
1905:6   2   2   5   0   3   5   1   4   6   2   4   | 2
1906:0   3   3   6   1   4   6   2   5   0   3   5   | 2
.
.
.
On normal years, the next year is the same as +1 to all the numbers
On leap years, it is +1 from Jan to Feb, but +2 everywhere else

So one could analyze it like so, find how many sundays are for each month over that period and sum them up.
Total = 14 + 14 + 15 + 13 + 14 + ...
January:
1 2 3 4

1 2 3 4 #1904
6 0 1 2 #1908
4 5 6 0 #1912
2 3 4 5 #1916
0 1 2 3 #1920
5 6 0 1 #1924
3 4 5 6 #1928

1 2 3 4 #1932
# For january, the cycle repeats every 28 years and the s = 4
# 100  % 28 = 16
# 100 // 28 = 3
# After 16 years , s = 2
# For the range of 1901 to 2000, it is : (4*3)+2 == 14

February: # +2 after leap
1 2 3 4

4 5 6 0
2 3 4 5
0 1 2 3
5 6 0 1
3 4 5 6
1 2 3 4
6 0 1 2

# S_28 = 4 , S_16 = 2 : (4*3)+2 == 14

March: # Feb, but + 2 at leap
4 5 6 1
2 3 4 6
0 1 2 4
5 6 0 2
3 4 5 0
1 2 3 5
6 0 1 3

# S_28 = 4 , S_16 = 3 : (4*3)+3 == 15

April: # +1 always, +2 at leap
0 1 2 4 # 1904
5 6 0 2 # 1908
3 4 5 0 # 1912
1 2 3 5 # 1916
6 0 1 3 # 1920
4 5 6 1 # 1924
2 3 4 6 # 1928

# Cycle len = 28 years
# S_28 = 4 , S_16 = 1, (4*3)+1 = 13

May: # +1 always, +2 at leap and same for rest of the months
2 3 4 6
0 1 2 4
5 6 0 2
3 4 5 0
1 2 3 5
6 0 1 3
4 5 6 1

S_28 = 4 , S_16 = 2 : (3*4)+2 = 14
...
Notice, that May = April+2, and likewise the rest of the values in the table for the rest of the months

if we take april as an example, if we add 2 to it to get may, the days that are 4 will constitute the new 6 and likewise
      The new 6, from April's perspective
April: 6
May  : 4
June : 1
July : 6
Aug  : 3
Sep  : 0
Oct  : 5
Nov  : 2
Dec  : 0

Now to make use of that, lets count all the (0,1,2,3,4,5,6) in April.
Turns out, they are perfectly evenly distributed. All of them are 4.
Since all of them are 4 and they all have the same amounts of each, every month april and after have the same amount of
sundays!

All of those months have 4 sundays per cycle.
Therefore:

total for those months, without considering the S_16 = 8*(3*4)
= 96
Total so far, w/o S_16 past april = 96 + 14 + 14 + 15
= 139

Now we must consider the S_16 for each month April and beyond

S_16 for april:

0 1 2 4 # 1904
5 6 0 2 # 1908
3 4 5 0 # 1912
1 2 3 5 # 1916

0: 3
1: 2
2: 3
3: 2
4: 2
5: 3
6: 1

The new 6 chart again:

      The new 6, from April's perspective
April: 6
May  : 4
June : 1
July : 6
Aug  : 3
Sep  : 0
Oct  : 5
Nov  : 2
Dec  : 0
                 0    1     2     3     4     5     6
Now the S_16 = (3*2)+(2*1)+(3*1)+(2*1)+(2*1)+(3*1)+(1*2)
=20 for each cycle len 16

S = 14 + 14 + 15 + 13 + 14 + 14 + 13 + 14 + 15 + 15 + 15 + 15
S = 171

  Jan: 14
  Feb: 14
  Mar: 15

April: 12+1 =13
  May: 12+2 =14
 June: 12+2 =14
  Jul: 12+1 =13
  Aug: 12+2 =14
  Sep: 12+3 =15
  Oct: 12+3 =15
  Nov: 12+3 =15
  Dec: 12+3 =15

Finally, it has been shown quite clearly that the answer is thus

171 Sundays

'''
print('There are 171 Sundays on the first of the month from 1 Jan 1901 to 31 Dec 2000')
