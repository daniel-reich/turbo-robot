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

def who_won(bd):
    lor = []
    for row in bd:
        lor.append(row)
    tbd = map(list, zip(*bd))
    for row in tbd:
        lor.append(row)
    lor.append([bd[0][0], bd[1][1], bd[2][2]])
    lor.append([bd[0][2], bd[1][1], bd[2][0]])
    
    for row in lor:
        if row[0] == row[1] == row[2]:
            return row[0]

