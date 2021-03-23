"""


Given a list containing three strings, representing the rows of an O's and X's
board from top to bottom, return the row and column position of the winning
move for X's. Return `False` if the game cannot be won.

### Examples

    x_and_o(board = [" | | ", " |X| ", "X| | "]) ➞  [1, 3]
    
    # Board becomes:
    #    |   |
    #    |X |
    # X |   |
    
    x_and_o(board = ["X|X|O", "O|X| ", "X|O| "]) ➞ [3, 3]
    
    # Board becomes:
    # X|X|O
    # O|X|
    # X|O|

### Notes

There is no 0 index for the row or column.

"""

def x_and_o(board):
  rows = [row.split('|') for row in board]
  cols = list(zip(*rows))
  diag1 = [[rows[0][0], rows[1][1], rows[2][2]]]
  diag2 = [[rows[2][0], rows[1][1], rows[0][2]]]
  combs = rows + cols + diag1 + diag2
​
  for i in range(len(combs)):
    if combs[i].count('X') == 2 and combs[i].count(' ') == 1:
      j = combs[i].index(' ')+1
      if combs[i] in rows:
        return [(i%3)+1, j]
      elif combs[i] in cols:
        return [j, (i%3)+1]
      elif combs[i] in diag1:
        return [j, j]
      elif combs[i] in diag2:
        return [4-j, j]
  return False

