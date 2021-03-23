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
import heapq as h
​
MULTIPLIER = sin(pi/8)  # unit for the interspoke distance
SPOKES = 'ABCDEFGH'
​
ring_dist = lambda r: r * 2 * MULTIPLIER  # distance between 2 spokes on ring r
​
def next_points(p):
    '''
    Returns a list of the points immediately reachable from p in the form (q, d)
    where q is the point and d its distance from p
    '''
    if p == 'A0':  # centre of web
        return [(q+'1', 1) for q in SPOKES]
​
    s, r = p
    r = int(r)
    if r == 4:
        distances = [(s+'3',1)]
    elif r == 1:
        distances = [('A0',1), (s+'2',1)]
    else:
        distances = [(s+str(r+1),1),(s+str(r-1),1)]  # moves along the spoke
        
    spokes = [SPOKES[(SPOKES.index(s)+i)%8] for i in (-1,1)]
    distances.extend([(spoke+str(r), ring_dist(r)) for spoke in spokes])
​
    return distances
    
def spider_vs_fly(spider, fly):
    '''
    Returns the path of the quickest route along the web from the spider to the fly
    Uses Dijkstra's algorithm to compute shortest distance.
    '''
    distances = {a+b: float('inf') for a in SPOKES for b in '1234'}
    distances['A0'] = float('inf')  # initialise all distances to infinity
    prev = {spider: -1}  # to track path
    q =[]
    distances[spider] = 0  # cumulative distance start
    h.heappush(q, (0, spider))  # start point in queue
​
    while q:
        this = h.heappop(q)[1]
        for point, distance in next_points(this):
            if distances[point] > distances[this] + distance:
                distances[point] = distances[this] + distance
                prev[point] = this
                h.heappush(q, (distances[point], point))
​
    next_point = fly
    path = []
    while next_point != -1:
        path.append(next_point)
        next_point = prev[next_point]   # build up path in reverse order
​
    return '-'.join(path[::-1])

