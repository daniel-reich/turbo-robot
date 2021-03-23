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

from collections import deque
​
def knight_bfs(a, b, c, d):
    dd = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2,-1)]
​
    board = [[0 for j in range(8+4)] for i in range(8+4)]
    path = [[None for j in range(8+4)] for i in range(8+4)]
    
    for i in range(8+4):
        board[0][i] = -1
        board[1][i] = -1
        board[8+4-1][i] = -1
        board[8+4-2][i] = -1
        
        board[i][0] = -1
        board[i][1] = -1
        board[i][8+4-1] = -1
        board[i][8+4-2] = -1
        
    q = deque([(a+2-1, b+2-1)])
    while len(q) > 0:
        node = q.popleft()
        if node[0] == c+2-1 and node[1] == d+2-1:
            break
        
        for delta in dd:
            x = node[0] + delta[0]
            y = node[1] + delta[1]
            
            if board[x][y] >= 0:
                board[x][y] = board[node[0]][node[1]] + 1
                q.append((x,y))
    
    return board[c+2-1][d+2-1]

