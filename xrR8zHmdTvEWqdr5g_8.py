"""


Given the shortest side of a 30 60 90 triangle you have to find out the other
2 sides, (return the longest side, medium-length side).

### Examples

    returnsides(1) ➞ (2, 1.73)
    
    returnsides(2) ➞ (4, 3.46)
    
    returnsides(3) ➞ (6, 5.2)

### Notes

  * 30 60 90 triangles always follow this rule, let's say the shortest side length is x units, the hypotenuse would be 2x units and the other side would be x * root3 units.
  * In the **Tests** , the decimal is rounded to 2 places.
  * Return the values as a tuple.

"""

def returnsides(length):
  return (length * 2, round(length * 3 ** 0.5, 2))

