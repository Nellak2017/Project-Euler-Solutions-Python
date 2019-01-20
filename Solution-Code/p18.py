# Project Euler Problem 18
# Max path sum in triangle of numbers

tri_num = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

for x in range(len(tri_num) - 1, -1, -1):
    for y in range(0, x):
        tri_num[x - 1][y] += max(tri_num[x][y], tri_num[x][y + 1])
print(tri_num[0][0])

'''
I break the big triangle into smaller triangles, working my way from the bottom up to the top. 
I take the max of the 2 possible numbers it could branch into and eliminate the smaller value, I do this for all values until I reach
the next level and so I repeat until the very top. 
ex:           .
     91   71  ...
      \   /
  x63  66    4   ...
    \    \  /
4    62   98 ...

Notice in the example that the 63 branch, on the row 2nd from the bottom and the col all the way to the left, was pruned.

This is a bottoms up, Dynamic Programming approach to solve the problem.

'''
