# Euler 38
# Aug 30 2018
'''
0.) n > 9183 [ref. problem description]
1.) The n,2n partition is the only valid partition and n must be 4 digits, in 9183 < n < 9487
    Proof:

    Partition -> Result
    4,6       -> 9183 < n < 9487
    3,3,3     -> (300 < n < 327) < 9183
    2,2,2,2,1 -> Impossible, n > 25
    2,2,2,3   -> Impossible, 25 < n < 33 , none are > 9183
    2,2,5     -> Impossible, 99*3 < 10**5
    2,6       -> Impossible, 99*2 < 10**6
    1,(x)     -> Impossible, n = 9 fails, so all the others must too
-- Tests:

94** -> no
93** -> maybe
937* -> no
936* -> no
935* -> no
934* -> no
932* -> Yes

>> n = 9327
>> answer = 932718654
'''
print(932718654)