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

class Insect:
  def __init__(self,insect):
    self.letter = insect[0]
    self.number = int(insect[1])
  def next_letter(self):
    return "A" if self.letter == "H" else chr(ord(self.letter)+1)
  def prev_letter(self):
    return "H" if self.letter == "A" else chr(ord(self.letter)-1)
  
def spider_vs_fly(spider, fly):
  s = Insect(spider)
  f = Insect(fly)
  lst = [spider]
  if s.number > f.number:
    lst.extend(list(map(lambda x: s.letter + str(x),range(s.number-1,f.number-1,-1))))
  if s.next_letter() != f.letter and s.prev_letter() != f.letter:
    if s.next_letter() == f.prev_letter():
      lst.append(s.next_letter() + str(f.number))
    elif s.prev_letter() == f.next_letter():
      lst.append(s.prev_letter() + str(f.number))
    else:
      if f.number > 1:
        lst.extend(list(map(lambda x: s.letter + str(x),range(f.number-1,0,-1))))
      lst.append("A0")
      if f.number > 1:
        lst.extend(list(map(lambda x: f.letter + str(x),range(1,f.number))))
  lst.append(fly)
  return '-'.join(lst)

