# Euler 57 , Square Root Convergents
# Aug 26 2019
# In Thailand Right now, bangkok. I love it! So much pussy!!
# Created by Connor Keenum

import math

def continuedfraction(x,precision=10):
    # returns linear form of continued fraction, in the form of a list
    # This is inaccurate at high precision
    answer = []
    t = 0; i = 0
    while (x - int(x)) != 0 and i <= precision:
        answer.append(int(x))
        x = 1 / (x - int(x))
        i += 1
    return answer

def convergents(v): # Modified from original to count the num numerators that have more digits than denominator
    # returns the partial convergents of a continued fraction in original version
    pp = 1; qq=0; p=v[0]; q=1
    answer = [0]*len(v)
    answer[0] = p/q

    # Modded bits
    sanswer = [str(p) + '/' + str(q)]
    sum = 0 # Holds how many times the numerator is bigger than the denominator
    # Original
    for n in range(1,len(v)):
        tp = p
        tq = q
        p = v[n] * p + pp
        q = v[n] * q + qq
        pp = tp
        qq = tq
        answer[n] = p/q
        # Modded bits
        sanswer.append(str(p)+'/'+str(q))
        if int(math.log(p,10)) > int(math.log(q,10)):
            sum += 1
    # Modded bits
    print(sanswer)
    return sum

a = [1] ; a += [2]*999 # We know the continued fraction for the sqrt(2). Applying original algo leads to precision error
print(a)
print(convergents(a))

# For this project euler problem, we made the continued fraction of sqrt(2) ourselves because
# the above implementation of continued fraction is inaccurate at high precision
# convergents seems to run fine at high precision
