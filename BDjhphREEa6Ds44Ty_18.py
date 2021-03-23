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
def bomb(lst):
    for i in range(3):
        if lst[i][2] == 0:
            return (lst[i][0],lst[i][1])
​
    x1 = lst[0][0]
    x2 = lst[1][0]
    x3 = lst[2][0]
    y1 = lst[0][1]
    y2 = lst[1][1]
    y3 = lst[2][1]
    r1 = lst[0][2]*.343
    r2 = lst[1][2]*.343
    r3 = lst[2][2]*.343
​
    x = round(abs(((y2-y3)*((y2**2-y1**2)+(x2**2-x1**2)+(r1**2-r2**2))-(y1-y2)*((y3**2-y2**2)+(x3**2-x2**2)+(r2**2-r3**2)))/(2*((x1-x2)*(y2-y3)-(x2-x3)*(y1-y2)))))
    y = round(abs(((x2-x3)*((x2**2-x1**2)+(y2**2-y1**2)+(r1**2-r2**2))-(x1-x2)*((x3**2-x2**2)+(y3**2-y2**2)+(r2**2-r3**2)))/(2*((y1-y2)*(x2-x3)-(y2-y3)*(x1-x2)))))
​
    return (x,y)

