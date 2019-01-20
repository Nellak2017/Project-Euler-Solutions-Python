# Project euler Problem 15
# number of node paths on a graph, size 20 x 20 
# runs in O(1)
# modified on Aug 25 2018
'''
Math:
Using MS Paint to visualize the nodal paths, it is deduced that the path of a current node is 
determined by the sum of the paths to the right and below it.
Starting with a 1 x 1 that is like this:

*2 *1
*1 *1
     1
 
Note, it looks like a pascal's triangle
extend to the 2 x 2 case:

*6 *3  *1
*3 *2  *1
*1 *1  *1 

For finding the path sum of the top left most node, it will thus be 2n choose n

0 : 0 choose 0 
1 : 2 choose 1
2 : 4 choose 2
...
n : 2n choose n

n choose k = n! / k!(n-k)!
therefore the closed form formula for this problem is:
2n choose k

where n = 20:

40 choose 20 = 137,846,528,820
'''
print(137846528820)
