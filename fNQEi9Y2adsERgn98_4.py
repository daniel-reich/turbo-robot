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
  point1 = lst[0]
  point2 = lst[1]
  point3 = lst[2]
  x1 = point1[0]
  y1 = point1[1]
  x2 = point2[0]
  y2 = point2[1]
  x3 = point3[0]
  y3 = point3[1]
  # dist --- point1 -> point2 ----- point2 -> point3 ----- point3 -> point1
  first_dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # point1 -> point2
  second_dist = math.sqrt((x2 - x3)**2 + (y2 - y3)**2) # point2 -> point3
  third_dist = math.sqrt((x3 - x1)**2 + (y3 - y1)**2) # point3 -> point1
  return round((first_dist + second_dist + third_dist),2)

