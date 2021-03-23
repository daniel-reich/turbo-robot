"""


Given three numbers, `x`, `y` and `z`, determine whether they are the edges of
a right angled triangle.

### Examples

    right_triangle(3, 4, 5) ➞ True
    # This is the classic example of a "nice" right angled triangle.
    
    right_triangle(145, 105, 100) ➞ True
    # This is a less famous example.
    
    right_triangle(70, 130, 110) ➞ False
    # This isn't a right angled triangle.

### Notes

  * Notice the largest side of the triangle might not be the last one passed to the function.
  * All numbers will be integers (whole numbers).

"""

def right_triangle(x, y, z):
  t = sorted([x, y, z])
  return t[0] ** 2 + t[1] ** 2 == t[2] ** 2 if all([ x > 0 for x in t ]) else False
