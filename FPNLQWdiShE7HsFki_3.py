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

ring_steps = [
    [0, 1, 2, 3, 4, -3, -2, -1],   
    [-1, 0, 1, 2, 3, 4, -3, -2],   
    [-2, -1, 0, 1, 2, 3, 4, -3],   
    [-3, -2, -1, 0, 1, 2, 3, 4],   
    [4, -3, -2, -1, 0, 1, 2, 3],   
    [3, 4, -3, -2, -1, 0, 1, 2],   
    [2, 3, 4, -3, -2, -1, 0, 1],
    [1, 2, 3, 4, -3, -2, -1, 0]
]
​
def spider_vs_fly(spider, fly):
    s0, s1 = "ABCDEFGH".index(spider[0]), int(spider[1])
    f0, f1 = "ABCDEFGH".index(fly[0]), int(fly[1])
    s2f_ring = ring_steps[s0][f0]
    s2f_radial = s1 - f1
    path = [spider]
    if abs(s2f_ring) > 2:
        # if angle between radii > 90 degrees always go via centre
        for i in range(s1-1, 0, -1):
            path.append(spider[0] + str(i))
        path.append("A0")
        s1 = 0
    else:
        if s2f_radial > 0:
            # if fly closer to centre move radially to same ring
            for i in range(s1-1, f1-1, -1):
                path.append(spider[0] + str(i))
                s1 = i
        # move along ring to fly's ring
        dirn = 1 if s2f_ring >= 0 else -1
        radial = s0
        while radial != f0:
            radial += dirn
            if radial < 0:
                radial += 8
            path.append("ABCDEFGH"[radial] + str(s1))
    # finally move radially to fly's ring and gobble
    for i in range(s1+1, f1+1):
        path.append(fly[0] + str(i))
    return "-".join(path)

