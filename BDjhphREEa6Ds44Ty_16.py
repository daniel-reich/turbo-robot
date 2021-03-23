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

import math
​
eps = 1e-1
v = 0.343
​
def dist(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
​
def bomb(lst):
    X, Y, T = [], [], []
    for x, y, t in lst:
        X.append(x)
        Y.append(y)
        T.append(t)
    for bx in range(51):
        for by in range(51):
            found = True
            for i in range(3):
                d = dist((bx, by), (X[i], Y[i]))
                if abs(d / v - T[i]) > eps:
                    found = False
                    break
            if found:
                return (bx, by)

