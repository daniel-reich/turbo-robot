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

def perimeter(lst):
  get_dist = lambda a,b: pow(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2), .5)
  p1,p2,p3 = lst
  return round(sum(get_dist(*c) for c in [(p1,p2), (p1,p3), (p2,p3)]), 2)

