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

from math import sin, pi
inner_edge = [i * 2 * sin(pi / 8) for i in range(5)]
grid = "ABCDEFGH"
​
def spider_vs_fly(spider, fly):
    s_radial, s_radius = spider[0], int(spider[1])
    f_radial, f_radius = fly[0], int(fly[1])
    s_idx = grid.index(s_radial)
    clockwise = 0
    while grid[(s_idx + clockwise) % 8] != f_radial:
        clockwise += 1
    counterwise = 0
    while grid[(s_idx - counterwise) % 8] != f_radial:
        counterwise += 1
    h_distance = min(clockwise, counterwise)
    direction = clockwise <= counterwise
    via_center = s_radius + f_radius
    min_r = min(s_radius, f_radius)
    via_edge = (abs(s_radius - min_r) + abs(f_radius - min_r)
                + h_distance * inner_edge[min_r])
    if via_center <= via_edge:
        return ("-".join("{}{}".format(s_radial, i)
                         for i in range(s_radius, 0, -1)) + "-A0-" +
                "-".join("{}{}".format(f_radial, i)
                         for i in range(1, f_radius + 1)))
    elif s_radius > min_r:
        res = "-".join("{}{}".format(s_radial, i)
                       for i in range(s_radius, min_r - 1, -1))
        if h_distance > 0:
            res += "-"
            res += "-".join("{}{}".format(grid[(s_idx +
                                                (step if direction else -step))
                                               % 8], str(min_r))
                            for step in range(1, h_distance + 1))
    else:
        res = "-".join("{}{}".format(grid[(s_idx +
                                          (step if direction else -step))
                                          % 8], str(min_r))
                       for step in range(h_distance + 1))
        if f_radius > min_r:
            res += "-"
            res += "-".join("{}{}".format(f_radial, i)
                            for i in range(min_r + 1, f_radius + 1))
    return res

