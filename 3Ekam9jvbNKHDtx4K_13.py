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

# Source Link : https://edabit.com/challenge/3Ekam9jvbNKHDtx4K
# Level : Medium
​
import math
​
def line_length(f_point , s_point):
  delta_x = s_point[0] - f_point[0]
  delta_y = s_point[1] - f_point[1]
​
  return round(math.sqrt(delta_x**2 + delta_y**2) , 2)

