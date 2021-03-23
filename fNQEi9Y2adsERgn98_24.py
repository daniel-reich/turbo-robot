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

from math import sqrt
def perimeter(lst):
  l1 = sqrt((lst[1][0]-lst[0][0])**2 + (lst[1][1]-lst[0][1])**2)
  l2 = sqrt((lst[2][0]-lst[1][0])**2 + (lst[2][1]-lst[1][1])**2)
  l3 = sqrt((lst[2][0]-lst[0][0])**2 + (lst[2][1]-lst[0][1])**2)
  return round(l1 + l2 + l3,2)

