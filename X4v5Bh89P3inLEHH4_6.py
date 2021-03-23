"""


Given a list of directions to spin, `"left"` or `"right"`, return an integer
of how many full **360°** rotations were made. Note that each word in the list
counts as a **90°** rotation in that direction.

### Worked Example

    spin_around(["right", "right", "right", "right", "left", "right"]) ➞ 1
    # You spun right 4 times (90 * 4 = 360)
    # You spun left once (360 - 90 = 270)
    # But you spun right once more to make a full rotation (270 + 90 = 360)

### Examples

    spin_around(["left", "right", "left", "right"]) ➞ 0
    
    spin_around(["right", "right", "right", "right", "right", "right", "right", "right"]) ➞ 2
    
    spin_around(["left", "left", "left", "left"]) ➞ 1

### Notes

  * Return a positive number.
  * All tests will only include the words `"right"` and `"left"`.

"""

import math
def spin_around(lst):
  angle = 0
  for turn in lst:
    if turn == "left":
      angle -= 90
    else:
      angle += 90
  return angle//360 if angle//360 >= 0 else abs(math.ceil(angle/360))

