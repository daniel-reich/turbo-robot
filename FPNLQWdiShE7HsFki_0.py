"""


A spider web is defined by **rings** numbered from **0-4** from the center and
**radials** labeled clock-wise from the top as **A-H**.

Create a function that takes the coordinates of `spider` and `fly` and returns
the shortest path for the spider to get to the fly.

It's worth noting that the shortest path should be calculated "geometrically",
not by counting the number of points that path goes through. We could arrange
that:

  * Angle between every pair of radials is the same (45 degrees).
  * Distance between every pair of rings is always the same (let's say "x").

![Mubashir](https://edabit-challenges.s3.amazonaws.com/aSAWPl0.png)

In the above picture, `spider` coordinates are **"H3"** and `fly` coordinates
are **"E2"**. The spider will follow the shortest path **"H3-H2-H1-A0-E1-E2"**
to reach the fly.

### Examples

    spider_vs_fly("H3", "E2") ➞ "H3-H2-H1-A0-E1-E2"
    
    spider_vs_fly("A4", "B2") ➞ "A4-A3-A2-B2"
    
    spider_vs_fly("A4", "C2") ➞ "A4-A3-A2-B2-C2"

### Notes

The center of the web will always be `A0`.

"""

def get_mod(x):
    return (ord(x) - 65) % 8
​
​
def get_letter(x):
    return chr(x + 65)
​
​
def sign(x):
    return 1 if x >= 0 else -1
​
​
def get_fast_path(s, f):
    s = get_mod(s)
    f = get_mod(f)
    cc = f - s
    c = max(s, f) - 8 - min(s, f)
    return cc if abs(cc) < abs(c) else c
​
​
def get_path_through_center(spider, fly):
    path = ""
    for i in range(int(spider[1]), 0, -1):
        path += "-{0}{1}".format(spider[0], i)
    path += "-A0"
    for i in range(1, int(fly[1]) + 1):
        path += "-{0}{1}".format(fly[0], i)
    return path[1:]
​
​
def get_path_through_face(spider, radial_route, ring_route, s_d, f_d):
    path = ""
    for i in range(s_d, s_d + radial_route + sign(radial_route), sign(radial_route)):
        path += "-{0}{1}".format(spider[0], i)
    s_m = get_mod(spider[0])
    for i in range(s_m + sign(ring_route), s_m + ring_route + sign(ring_route), sign(ring_route)):
        path += "-{0}{1}".format(get_letter(i % 8), f_d)
    return path[1:]
​
​
def spider_vs_fly(spider, fly):
    s_d = int(spider[1])
    f_d = int(fly[1])
    ring_route_path_length = get_fast_path(spider[0], fly[0])
    radial_route_path_length = f_d - s_d
    if pow(pow(min(s_d, f_d), 2) * (2 - pow(2, 0.5)), 0.5) * abs(ring_route_path_length) + abs(
            radial_route_path_length) > s_d + f_d:
        return get_path_through_center(spider, fly)
    else:
        return get_path_through_face(spider, radial_route_path_length, ring_route_path_length, s_d, f_d)

