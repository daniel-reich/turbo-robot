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

import numpy as np
​
def knight_bfs(x1,y1,x2,y2):
    steps = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
    board = np.ones((9,9),dtype=np.int16)*10000
    board[x1][y1] = 0
    work_list = []
    for i in range(1,9):
        for j in range(1,9):
            work_list.append([i, j])
    
    while(len(work_list) !=0):
        min_index = 0
        min_number = 10000
        for i,ele in enumerate(work_list):
            x = ele[0]
            y = ele[1]
            if board[x][y] < min_number:
                min_number = board[x][y]
                min_index = i
        x,y = work_list.pop(min_index)
        #print(x,y,board[x][y])
        for ele in steps:
            x_new = x + ele[0]
            y_new = y + ele[1]
            if (x_new >= 1 and x_new <=8) and (y_new >= 1 and y_new <=8):
                if board[x][y] + 1 <= board[x_new][y_new]:
                    board[x_new][y_new] = board[x][y] + 1
    
        
    return board[x2][y2]

