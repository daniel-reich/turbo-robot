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

def bug_jump(height, time):
  a=height**.5
  time=time/1000
  y=round(height-(time-a)**2,2)
  if y%1==0:
    y=int(y)
  v=-2*(time-a)
  if y>=0:
    if v>0:
      return [y, 'up']
    else:
      return [y, 'down']
  else:
    return [0, None]

