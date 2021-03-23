"""


Create a function that takes a Tic-tac-toe board and returns `"X"` if the X's
are placed in a way that there are three X's in a row or returns `"O"` if
there is three O's in a row.

### Examples

    who_won([
      ["O", "X", "O"],
      ["X", "X", "O"],
      ["O", "X", "X"]
    ]) ➞ "X"
    
    who_won([
      ["O", "O", "X"],
      ["X", "O", "X"],
      ["O", "X", "O"]
    ]) ➞ "O"

### Notes

  * There are no Ties.
  * All places on the board will have either "X" or "O".
  * Check **Resources** for more info.

"""

def who_won(b):
  for r in b:
    if len(set(r)) == 1:  return r[0]
    
  for c in zip(*b):
    if len(set(c)) == 1: return c[0]
  
  if b[0][0] == b[1][1] == b[2][2]: return b[0][0]
  
  if b[0][2] == b[1][1] == b[2][0]: return b[0][2]

