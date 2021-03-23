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

def bomb(data):
    '''
    Given the coordintes of 3 points plus the time taken for a bomb blast to
    reach them, return a tuple giving the bomb's location as described above.
    '''
    # Trilateration formula courtesy of https://math.stackexchange.com/
    # questions/884807/find-x-location-using-3-known-x-y-location-using-
    # trilateration
    
    SOUND_SPEED = 0.343
​
    p1, p2, p3 = data
    x1, y1, r1 = p1[0], p1[1], p1[2] * SOUND_SPEED
    x2, y2, r2 = p2[0], p2[1], p2[2] * SOUND_SPEED
    x3, y3, r3 = p3[0], p3[1], p3[2] * SOUND_SPEED  # coordinates & distance
​
    if r1 == r2 == r3 == 0.0:
        return (x1, y1)   # they are all on top of the bomb!
​
    A = -2*x1 + 2*x2
    B = -2*y1 + 2*y2
    C = r1*r1 - r2*r2 - x1*x1 + x2*x2 - y1*y1 + y2*y2
    D = -2*x2 + 2*x3
    E = -2*y2 + 2*y3
    F = r2*r2 - r3*r3 - x2*x2 + x3*x3 - y2*y2 + y3*y3
​
    return (round((C*E - F*B) / (E*A - B*D)), round((C*D - A*F) / (B*D - A*E)))

