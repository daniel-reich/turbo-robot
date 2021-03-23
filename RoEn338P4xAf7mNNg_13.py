"""


Given a rectangular grid of m by n spaces, signaled by 0s, and a number of
points, signaled by 1, 2, 3..., return the number of moves for the shortest
path that starts at 1 and goes over all the other points in ascending order.

### Examples

    shortest_path([
      ("001"),
      ("002"),
      ("003")
    ]) ➞ 2
    
    shortest_path([
      ("00000"),
      ("01006"),
      ("02000"),
      ("30050"),
      ("00004")
    ]) ➞ 13
    
    shortest_path([
      ("00020000"),
      ("01000000")
    ]) ➞ 3

### Notes

  * Only horizontal and vertical movements are allowed.
  * All movements from one place to an adjacent one count as 1 regardless of direction.
  * The points range from 1 to at most 9 with no repeating or missing digits.

"""

def shortest_path(lst):
    c='';a=1;ans=0
    le=len(lst[0])
    for i in lst:
        c+=i
    p=c.find('1')
    x=p//le
    y=p%le
    while a<int(sorted(c)[-1]):
        a+=1
        p=c.find(str(a))
        x1=p//le
        y1=p%le
        ans+=abs(x-x1)+abs(y-y1)
        x,y=x1,y1
    return ans

