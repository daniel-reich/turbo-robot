"""


Write a function that returns `True` if the knights are placed on a chessboard
such that **no knight can capture another knight**. Here, `0`s represent empty
squares and `1`s represent knights.

### Examples

    cannot_capture([
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 0]
    ]) ➞ True
    
    cannot_capture([
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 1, 0, 1]
    ]) ➞ False

### Notes

  * Knights can be present in any of the 64 squares.
  * No other pieces except knights exist.

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
def cannot_capture(board):
    '''
    Returns True if any knight on the board can capture any other knight
    as per instructions.
    '''
    knight_locs = [(i,j) for i in range(8) for j in range(8) \
                   if board[i][j]]
    
    if knight_locs:  # at least 1 knight present
        attack_locs = [knight_moves(i,j) for i,j in knight_locs]
        attack_locs = set([knight for knights in attack_locs for knight in knights])
        return all(knight not in attack_locs for knight in knight_locs)
​
    return True

