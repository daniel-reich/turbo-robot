"""


When a bug jumps to a `height` _y_ , its position can be plotted as a
quadratic function with _x_ as the `time`, and _y_ as the vertical distance
traveled. For example, for a bug that jumps 9 cm up and is back on the ground
after 6 seconds, its trajectory can be plotted as:

![bug jump quadratic plot](https://edabit-images.s3.amazonaws.com/2pMgjmZ.png)

Create a function that, given the max height of a vertical jump in cm and the
current time in milliseconds, returns the current position of the bug rounded
to two decimal places, and its direction (`"up"` or `"down"`). If the bug is
already back on the ground, return `0` for the position and `None` for the
direction.

### Examples

    bug_jump(9, 1000) ➞ [5, "up"]
    
    bug_jump(9, 4000) ➞ [8, "down"]
    
    bug_jump(9, 5500) ➞ [2.75, "down"]
    
    bug_jump(9, 7000) ➞ [0, None]

### Notes

  * Time and position both start at `0`.
  * You only need to translate the parabola (you don't need to scale it).

"""

import math
​
# gravity acceleration from example in specs:
g = 2.0 * 9.0 / 3.0**2
​
def bug_jump(height, time):
    time /= 1000.
    v = math.sqrt(2.0 * height * g)
    t_top = v / g
    if time >= 2 * t_top:
        return [0, None]
    y = round(abs(time**2 - time * 2 * t_top), 2)
    if time <= t_top:
        return [y, "up"]
    else:
        return [y, "down"]

