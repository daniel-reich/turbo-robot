"""


Create a function that takes three numbers as arguments and returns `True` if
it's a triangle and `False` if not.

### Examples

    is_triangle(2, 3, 4) ➞ True
    
    is_triangle(3, 4, 5) ➞ True
    
    is_triangle(4, 3, 8) ➞ False

### Notes

  * `a`, `b` and, `c` are the side lengths of the triangles.
  * Test input will always be three positive numbers.

"""

def is_triangle(a, b, c):
  if a  + b  > c:
    if b + c > a:
      if a + c > b:
        return True
  return False

