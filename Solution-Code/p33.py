# Euler 33
# Aug 28 2018

'''
49/98 -> cancel 9's == 4/8
so if len(set(str(a)) - set(str(b))) == 2: We may proceed in cancelling
a < b for the answer to be less than 1

product = 1
for a in range(1,99):
    for b in range(1,99):
        if a < b:
            d = set(str(a))
            e = set(str(b))
            if len(d ^ e) == 2):
                c = sorted(d^e) # Note: a and b are strings in the set
                if int(c[0])/int(c[1]) == a/b:
                    print(a,'/',b)
                    product *= b
print('product =',product)

a = {'4','9'}
b = {'9','8'}
a ^ b = {'4','8'}
Since a < b, sorted(set(a^b)) =  c
 if c[0]/c[1] = a/b # Considering the original int versions
    print(a,'/',b)
    product *= b
'''
product = 1
for a in range(10,99):
    for b in range(10,99):
        if a < b:
            foo = str(a)
            bar = str(b)
            if int(foo[-1]) != 0 and int(bar[-1]) != 0 :
                test = int(bar[-1])%int(foo[-1]) == 0
            test_1 = int(foo[0]) == int(foo[1]) or int(bar[0]) == int(bar[1])
            d = set(str(a))
            e = set(str(b))
            if len(d ^ e) == 2 and int(foo[-1]) != 0 and not test and not test_1:
                c = sorted(d^e) # Note: a and b are strings in the set
                if int(c[0])/int(c[1]) == a/b:
                    print(a,'/',b)
                    product *= a/b
print('product =',product)

'''
16 / 64
19 / 95
26 / 65
49 / 98

2/4 * 1/5 * 2/5 * 1/4
=
4/400
=
100
'''
print('answer is 100')