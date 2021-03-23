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
  movs = [[1,2], [1,-2], [2,1], [2,-1], [-1,2], [-1,-2], [-2,1], [-2, -1]]
  known = []
  toche = []
  known.append([a, b])
  toche.append([a, b])
  print (a, " ", b)
  while len(toche) > 0 :
    print(toche)
    che = toche[0]
    for move in movs:
      print(move)
      nx = che[0] + move[0]
      print(nx)
      ny = che[1] + move[1]
      print(nx, " " ,ny)
      if (1 <= nx <= 8) and (1 <= ny <= 8):
        if [nx, ny] not in known :
          known.append([nx, ny])
          toche.append([nx, ny])
    del toche[0]
    print(known)
    print(toche)
    exit()

