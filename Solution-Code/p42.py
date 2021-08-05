# Euler 42
# Aug 31 2018
import Euler_Lib as foo
# turn the string of words into a list of python strings
with open('words.txt','r') as f:
    words = f.read().split(',')
    words = [list(word.strip('\"')) for word in words]
    f.close()

m = max([len(word) for word in words])
triangles = [foo.t(n) for n in range(1, 2 * m)]

vals = {}
s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for c in s:
    vals[c] = s.index(c) + 1

triangle_words = 0
for word in words:
    if sum([vals[c] for c in word]) in triangles:
        triangle_words += 1

print(triangle_words)