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

def spider_vs_fly(spider, fly):
  label = "ABCDEFGH"
  d = 4 - abs(4 - abs(label.index(spider[0]) - label.index(fly[0])))
  path = [spider]
​
  if abs(int(spider[1]) - int(fly[1]) > 0):
    while spider[1] != fly[1]:
      spider = spider[0] + str(int(spider[1]) - 1)
      path.append("A0" if spider[1] == "0" else spider)
​
  if d > 2:
    while spider[1] != "0":
      spider = spider[0] + str(int(spider[1]) - 1)
      path.append("A0" if spider[1] == "0" else spider)
​
    while spider != fly:
      spider = fly[0] + str(int(spider[1]) + 1)
      path.append(spider)
  else:
    a = label.index(spider[0])
    clockwise = label[(a + d) % 8] == fly[0]
​
    while spider != fly:
      a = (a + (1 if clockwise else -1)) % 8
      spider = label[a] + spider[1]
      path.append(spider)
​
  return "-".join(path)

