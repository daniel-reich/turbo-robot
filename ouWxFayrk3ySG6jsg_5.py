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
  a=list(zip(b[0],b[1],b[2]))
  c=[b[i][j] for i in range(len(a)) for j in range(len(a)) if i==j] 
  d=[b[i][j] for i in range(len(a)) for j in range(len(a)) if i+j==2]
  
  if len(set(c))==1:
    return c[0]
  if len(set(d))==1:
    return d[0]
  
  for i in range(len(b)):
    if len(set(a[i]))==1:
      return a[i][0]
    if len(set(b[i]))==1:
      return b[i][0]

