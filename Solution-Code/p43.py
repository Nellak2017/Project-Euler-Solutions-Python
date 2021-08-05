# Euler 43
# Aug 31 2018
# Substring divisiblity
# d1d2d3..dn = the nth digits in a 0 to 9 pandigital
'''
1.) d4d5d6 must be divisible by 5, d6 = 0 or 5
2.) d6d7d8 must be divisible by 11, and from observation 1 we
    know that d6 is either 0 or 5.
    if d6 is 0 then the only results are the set {011,022,..} and those
    are not pandigital numbers,
    d6 == 5
3.) Since d6 is 5 that limits d6d7d8 are limited to the five-hundreds
    divisible by 11 with no repeated digits which gives
    {506,517,528,539,561,572,583,594}
4.) d7d8d9 has to be divisible by 13 and from observation 3 we know
    we have limited d7d8 to 8 combos. That means we have a max 8
    sequences for d7d8d9. We can limit d6d7d8d9 to the set of 4
    sequences {5286,5390,5728,5832} by eliminating seq with repeated digits
5.) Repeating the above for d8d9d10 we get that d6d7d8d9d10 must be
    in the set {528867,53901,57289} so now we have limited the set to
    3 possible endings of the pandigital number.
6.) d5d6d7 must be divisible by 7 and must end on 52,01 or 89.
    That property limits our ending sequence to d5d6d7d8d9d10
    {952867, 357289}
7.) Since d2d3d4 has to be divisible by 2 it means that d4 must be
    even.
    {0952867,4952867,035729,4357289,6357289}
8.) d3d4d5 is divisible by 3.
    it ends on {09,49,03,43,63}
    based on the digit sum, we know that the sum d3+d4+d5 % 3 ==0
    for the number to be divisible by 3
    {30952867,60357289,06357289}
9.) The 3 entries in the set of possible endings have the common
    thing that none of them contain 1 or 4. Since there are no
    rules for d1 and d2, we can have both permutations of the
    two numbers and still have a valid number. That gives us
    a total of 6 numbers we need to sum up for the result.


result = 1430952867 + 1460357289 + 1406357289 + 4130952867
+ 4160357289 + 4106357289
= 16695334890
'''
print(16695334890)