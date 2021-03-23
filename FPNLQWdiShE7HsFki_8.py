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

def sign(a):
  if a==0:return 0
  return (a)//abs(a)
​
def radial(txt,s,f):
  return [txt +str(s-x*sign(s-f)) for x in range(abs(s-f)+1)]
​
def rotation(x,s,f):
  side_diff=abs(ord(s)-ord(f))
  if abs(ord(s)-ord(f)) >4:
    incr=-1
    side_diff=8-side_diff
  else: 
    incr=1
  return [ chr((ord(s)-ord('A')+(i+1)*incr)%8+ord('A'))+str(x) for i in range(side_diff)]
    
​
def spider_vs_fly(spider, fly):
  side=(1+1-2**0.5)**0.5
  side_diff=abs(ord(spider[0])-ord(fly[0]))
​
  if side_diff>4:side_diff=8-side_diff
  s=int(spider[1])
  f=int(fly[1])
  sf=min(s,f)
​
  if sf*side_diff*side + abs(s-f) < s+f: # side way shorter than over A0
    if s>=f:
      out=radial(spider[0],s,f)+rotation(f,spider[0],fly[0])
    else:
      out=[spider] + rotation(s,spider[0],fly[0])
      out.pop()
      out+=radial(fly[0],s,f)
  else: # over A0
    out=radial(spider[0],s,1) + ["A0"] + radial(fly[0],1,f)
      
  return('-'.join(out))

