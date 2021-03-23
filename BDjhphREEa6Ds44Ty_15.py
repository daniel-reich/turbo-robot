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
    distance1 = lst[0][2] * 0.343
    distance2 = lst[1][2] * 0.343
    distance3 = lst[2][2] * 0.343
    for i in range(51):
        for b in range(51):
            asquared = ((i-lst[0][0]) ** 2)
            bsquared = ((b-lst[0][1]) ** 2)
            csquared = round(distance1 ** 2)
            if asquared + bsquared == csquared:
                asquared = ((i-lst[1][0]) ** 2)
                bsquared = ((b-lst[1][1]) ** 2)
                csquared = round(distance2 ** 2)
                if asquared + bsquared == csquared:
                    asquared = ((i-lst[2][0]) ** 2)
                    bsquared = ((b-lst[2][1]) ** 2)
                    csquared = round(distance3 ** 2)
                    if asquared + bsquared == csquared:
                        return i, b

