"""


A large flat field measures _50x50_ kilometers. At a time `t = 0`, a bomb
explodes somewhere on the field. There are 3 scattered sensors with
synchronized clocks that record the exact time (in seconds) that the sound of
the exploding bomb reaches them.

Given the _x, y_ coordinates of each of the 3 sensors and the recorded time of
each, find the location of the bomb:

    bomb([[x1, y1, t1], [x2, y2, t2], [x3, y3, t3]]) ➞ (xb, yb)
    # Bomb location

### Examples

    bomb([[0, 0, 72.886], [0, 50, 72.886], [25, 25, 72.886]]) ➞ (0, 25)
    
    bomb([[0, 50, 145.773], [50, 50, 206.154], [50, 0, 145.773]]) ➞ (0, 0)
    
    bomb([[5, 8, 48.872], [12, 21, 35.107], [24, 20, 22.203]]) ➞ (21, 13)
    
    bomb([[18, 42, 35.558], [39, 16, 106.004], [7, 24, 32.202]]) ➞ (8, 35)

### Notes

  * The origin is at one corner of the square field so all the coordinates are positive integers in km units.
  * The bomb's coordinates are integers.
  * The speed of sound in air is 0.343 km/sec.

"""

def line_intersect(l1, l2):
  m1, b1 = l1
  m2, b2 = l2
  x = (b2 - b1) / (m1 - m2)
  return (round(x), round(m1 * x + b1))
​
def circles_intersect(c1, c2):
  x1, y1, r1 = c1
  x2, y2, r2 = c2
  dy = (y2 - y1) or 0.000001
  return ((x1 - x2)/dy, (r1**2 - x1**2 - y1**2 - r2**2 + x2**2 + y2**2) / (2 * dy))
​
def bomb(lst):
  if lst[0][2] == 0: return (lst[0][0], lst[0][1])
  if lst[1][2] == 0: return (lst[1][0], lst[1][1])
  if lst[2][2] == 0: return (lst[2][0], lst[2][1])
  for s in lst:
      s[2] *= 0.343
  return line_intersect(circles_intersect(lst[0], lst[1]), circles_intersect(lst[0], lst[2]))

