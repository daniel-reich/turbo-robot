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

def knight_moves(i, j):
    '''
    Returns a list of coordinates of the moves a knight can make from this
    location. Coordinates 1 to 8 in each dimension.
    '''
    possibles = ((2,1),(1,2),(-1,2),(-2,1),
                 (-2,-1),(-1,-2),(1,-2),(2,-1))
​
    return [(r+i,c+j) for r, c in possibles if 1 <= r+i <= 8 and 1 <= c+j <= 8]
​
GRAPH = {(i,j): knight_moves(i, j) for i in range(1,9) for j in range(1,9)}
#print(GRAPH)
​
def knight_bfs(start_i, start_j, end_i, end_j):
    '''
    Returns the minimum number of moves needed to legitimately move a knight
    from start to end as per instructions.
    '''
    visited = set()
    q = [(start_i, start_j)]
    prev = {square: -1 for square in GRAPH}  # to store path.
    
    while q:
        r, c = q.pop(0)
        if (r, c) == (end_i, end_j):  # reached target square
            count = 0
            square = (end_i, end_j)
            
            while prev[square] != -1:
                count += 1
                square = prev[square]
​
            return count
​
        visited.add((r, c))
        for k, l in GRAPH[(r, c)]:
            if (k, l) not in visited:
                prev[(k, l)] = (r, c)
                q.append((k, l))   # queue bfs order
​
    raise ValueError   # no path found - error!!

