"""


Write a function that takes the coordinates of three points in the form of a
2d array and returns the perimeter of the triangle. The given points are the
vertices of a triangle on a two-dimensional plane.

### Examples

    perimeter( [ [15, 7], [5, 22], [11, 1] ] ) ➞ 47.08
    
    perimeter( [ [0, 0], [0, 1], [1, 0] ] ) ➞ 3.42
    
    perimeter( [ [-10, -10], [10, 10 ], [-10, 10] ] ) ➞ 68.28

### Notes

  * The given points always create a triangle.
  * The numbers in the argument array can be positive or negative.
  * Output should have 2 decimal places
  * This challenge is easier than it looks.

"""

import math
def perimeter(lst):
   lst.append(lst[0])
   return round(sum([f(lst[i], lst[i+1])
           for i in range(len(lst)-1)]), 2)      
​
def f(p1, p2):
   x1, y1 = p1
   x2, y2 = p2
   return math.hypot(x2-x1, y2-y1)

