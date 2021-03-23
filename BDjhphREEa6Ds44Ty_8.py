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
    for i in lst:
        if i[2] == 0:
            return i[0],i[1]
    d = [0.343 * i[2] for i in lst]
    x1, x2, x3 = lst[0][0], lst[1][0] ,lst[2][0]
    y1, y2, y3 = lst[0][1], lst[1][1] ,lst[2][1]
    k1 = -1 * x1 ** 2 + x2 ** 2 + d[0] ** 2 - d[1] ** 2 - y1 ** 2 + y2 ** 2
    k2 = -1 * x1 ** 2 + x3 ** 2 + d[0] ** 2 - d[2] ** 2 - y1 ** 2 + y3 ** 2
    k3 = 2 * (x2 - x1)
    k4 = 2 * (y2 - y1)
    k5 = 2 * (x3 - x1)
    k6 = 2 * (y3 - y1)
    x_coord = (k1 - k2 * k4 / k6) / (k3 - k5 * k4 / k6)
    if k4 != 0:
        y_coord = (-1 * (k3 * x_coord) + k1) / k4
    else:
        y_coord = (-1 * (k5 *x_coord) + k2) / k6 
    return round(x_coord),round(y_coord)

