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

def bomb(lst):
  p1,p2,t1 = lst[0]
  q1,q2,t2 = lst[1]
  r1,r2,t3 = lst[2]
  if t1 == 0: return (p1,p2)
  mat = [[2*(q1-p1), 2*(q2-p2), (0.343*t1)**2 - (0.343*t2)**2-p1**2 -p2**2+q1**2+q2**2]]
  mat += [[2*(r1-p1), 2*(r2-p2), (0.343*t1)**2 - (0.343*t3)**2-p1**2-p2**2+r1**2+r2**2]]
  x = (mat[0][2]*mat[1][1]-mat[1][2]*mat[0][1])/(mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1])
  y =-(mat[0][2]*mat[1][0]-mat[1][2]*mat[0][0])/(mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1])
  return (round(x,1),round(y,1))

