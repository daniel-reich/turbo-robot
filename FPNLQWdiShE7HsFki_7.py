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

def spider_vs_fly(s, f):
  d='ABCDEFGH'
  si, fi=d.index(s[0]), d.index(f[0])
  sn, fn=int(s[1]), int(f[1])
  k=min(abs(si-fi), 8-abs(si-fi))
  path=[]
  if k>2:
    for i in range(sn, 0,-1):
      path.append('{}{}'.format(s[0],i))
    path.append('A0')
    for i in range(1, fn+1):
      path.append('{}{}'.format(f[0],i))
  elif 0<k<3:
    if k==abs(si-fi):
      if si>fi and sn>=fn:
        for i in range(sn,fn-1,-1):
          path.append('{}{}'.format(s[0],i))
        for i in range(si-1,fi-1,-1):
          path.append('{}{}'.format(d[i],fn))
      elif si>fi and sn<=fn:
        for i in range(si,fi-1,-1):
          path.append('{}{}'.format(d[i],sn))
        for i in range(sn+1,fn+1):
          path.append('{}{}'.format(f[0],i))
      elif si<fi and sn>=fn:
        for i in range(sn,fn-1,-1):
          path.append('{}{}'.format(s[0],i))
        for i in range(si+1,fi+1):
          path.append('{}{}'.format(d[i],fn))
      elif si<fi and sn<=fn:
        for i in range(si,fi-1,-1):
          path.append('{}{}'.format(d[i],sn))
        for i in range(sn-1,fn-1,-1):
          path.append('{}{}'.format(s[0],i))
          
  return '-'.join(path)

