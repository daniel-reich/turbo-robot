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
  a,b,c = lst
  ret = dist(a,b)
  ret += dist(b,c)
  ret += dist(a,c)
  return round(ret,2)
  
def dist(a,b):
  x1,y1 = a
  x2,y2 = b
  return ((x2-x1)**2+(y2-y1)**2)**(1/2)

