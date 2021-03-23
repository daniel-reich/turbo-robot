"""


Imagine a circle and two squares: a smaller and a bigger one. For the smaller
one, the circle is a circumcircle and for the bigger one, an incircle.

![Scale](https://edabit-challenges.s3.amazonaws.com/scale.png)

Create a function, that takes an integer (radius of the circle) and returns
the difference of the areas of the two squares.

### Examples

    square_areas_difference(5) ➞ 50
    
    square_areas_difference(6) ➞ 72
    
    square_areas_difference(7) ➞ 98

### Notes

Use only positive integer parameters.

"""

import math
def square_areas_difference(r):
  return ((r*2)**2) - round(math.sqrt((r**2)*2)**2)
  ## the first digit is area of larger square, second is the smaller square
  ## output of math.sqrt() is not an integer, so round() is used to get a correctly rounded int

