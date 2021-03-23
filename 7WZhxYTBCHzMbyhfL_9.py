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
    boa = [[0]*8 for i in range(8)]
    row = len(boa); col = len(boa[0]); sta = (a-1, b-1); end = (c-1, d-1)
    mov = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    que = [sta]; vis = {sta: []}
    while que:
        i, j = que.pop(0)
        nei = [(i+x, j+y) for x, y in mov if 0 <= i+x < row and 0 <= j+y < col]
        for n in nei:
            if n not in vis: vis[n] = vis[(i, j)] + [n]; que.append(n)
            if n == end: return len(vis[n])

