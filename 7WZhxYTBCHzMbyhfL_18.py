"""


You will be given the location of a knight, and an end location. The knight
can move in a "L" shape. "L" shape movement means that the knight can change
it's `x` coordinate by 2 and it's `y` coordinate by 1 or it can change it's
`y` coordinate by 2 and it's `x` coordinate by 1 (you can add and subtract
from the x/y).

For example, if the knight is at the position (0, 0), it can move to:

    (1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)

Your job is to return the least amount of steps needed to go from the position
K (knight's start position) to E (end). You will only be given the knight
starter coordinates (x1, y1) and the end coordinates (x2, y2).

Constrains: `1 <= x1,y1,x2,y2 <= 8`

### Examples

    knight_bfs(1, 1, 8, 8) ➞ 6
    
    knight_bfs(1, 1, 3, 2) ➞ 1
    
    knight_bfs(8, 8, 3, 3) ➞ 4

### Notes

  * This is a simplified version of [this problem](https://www.spoj.com/problems/NAKANJ/).
  * This travel will always be possible.
  * The chess board is 8x8.

"""

def knight_bfs(a, b, c, d):
  lst = [[a,b]]
  steps = 0
  while [c,d] not in lst:
    steps += 1
    temp = []
    for i in lst:
      temp+=[x for x in find_options(i[0],i[1]) if x not in lst]
    lst += temp
  return steps
    
def find_options(x,y):
  lst = []
  if x-1 > 0:
    if y-2 > 0:
      lst.append([x-1,y-2])
    if y+2 < 8:
      lst.append([x-1,y+2])
  if x+1 <= 8:
    if y-2 > 0:
      lst.append([x+1,y-2])
    if y+2 <= 8:
      lst.append([x+1,y+2])
  if x-2 > 0:
    if y-1 > 0:
      lst.append([x-2,y-1])
    if y+1 <= 8:
      lst.append([x-2,y+1])
  if x+2 <= 8:
    if y-1 > 0:
      lst.append([x+2,y-1])
    if y+1 <= 8:
      lst.append([x+2,y+1])
  return lst

