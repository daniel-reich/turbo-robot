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
  def myfunc (a,b):
    return (a-b)**2
  p = (sum(map(myfunc,lst[0],lst[1])))**0.5
  q = (sum(map(myfunc,lst[0],lst[2])))**0.5
  r = (sum(map(myfunc,lst[1],lst[2])))**0.5
  return round(p+q+r, 2)

