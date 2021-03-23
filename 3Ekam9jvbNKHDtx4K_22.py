"""


Write a function that takes coordinates of two points on a two-dimensional
plane and returns the length of the line segment connecting those two points.

### Examples

    line_length([15, 7], [22, 11]) ➞ 8.06
    
    line_length([0, 0], [0, 0]) ➞ 0
    
    line_length([0, 0], [1, 1]) ➞ 1.41

### Notes

  * The order of the given numbers is X, Y.
  * This challenge is easier than it looks.
  * Round your result to two decimal places.

"""

def line_length(dot1, dot2):
  return round(sum([(dot1[i]-dot2[i])**2 for i in range(len(dot1))])**0.5,2)

