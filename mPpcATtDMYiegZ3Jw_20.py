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
  
  if (x <= 0) or (y <= 0) or (z <= 0):
    return False
  
  Numbers = []
  Numbers.append(x)
  Numbers.append(y)
  Numbers.append(z)
  
  Numbers = sorted(Numbers)
  
  Value_A = Numbers[0] * Numbers[0]
  Value_B = Numbers[1] * Numbers[1]
  Value_C = Numbers[2] * Numbers[2]
  
  if (Value_A + Value_B == Value_C):
    return True
  else:
    return False

