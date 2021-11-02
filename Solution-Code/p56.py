#Euler 56
#Sep 27 2018

'''
For natural numbers, a^b ; a,b < 100, what is the maximum digital sum?

The computer approach is an obvious nested 2 for loop, but I want to be clever.
 digitSum( 99^99 ) = 936
 936 / 9  = 104 , so the min spaces needed is 104
 therefore, the number must be greater than 10^104
 So for all n < 12, are eliminated
 The maximum digital sum for n = 99 is x = 95 -> 972
 so the min spaces need is 108
 therefore, the number must be greater than 10^108
 So for all n < 14 are eliminated
 What about x? what are it's lower bound?
 Well that's equivalent to asking this:
 for a in range 14 to 99
 for b in range 1 to 99
 what is the minimum b to get a^b > 10^108 ?
 b ~ 248.679 / log(a)
 for a = 14 -> 94
 for a = 99 -> 54
 So it can be therefore concluded that in a^b, b > 53
 The search space is now 4042 vs the original 10000
'''
def digitSum(n):
    return int(sum(list(map(int,str(n)))))

def main():
    maxnum = 0
    maxgum = 0
    maxsum = 0
    for i in range(14,100):
        for j in range(53, 100):
            if digitSum(i**j) > maxsum:
                maxsum = digitSum(i**j)
                maxnum = i
                maxgum = j
    print(maxnum,'^',maxgum,'=',maxsum)

main()