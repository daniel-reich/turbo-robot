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

class Cell:
​
    def __init__(self, x,y,dist=0):
        self.x = x
        self.y = y
        self.dist = dist
​
​
def inbounds(nx, ny):
​
    return 1 <= nx <= 8 and 1 <= ny <= 8
​
def knight_bfs(a, b, c, d):
    pos = Cell(a,b,0) 
    queue = [pos]
    visited = [pos]
    moves = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)]
​
    while queue:
        pos = queue.pop(0)
        neighbors = [(pos.x+x, pos.y+y) for x,y in moves if inbounds(pos.x+x, pos.y+y)]
        for neighbor in neighbors:
            if neighbor == (c,d):
                return pos.dist + 1
            
            if neighbor not in visited:
                visited.append(neighbor)
                q,w = neighbor
                queue.append(Cell(q,w, pos.dist+1))
                
    return pos.dist

