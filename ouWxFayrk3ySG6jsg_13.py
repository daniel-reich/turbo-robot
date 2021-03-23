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

def who_won(a):
        for i in range(0,3):
                if (len(set(a[i]))==1) or (a[0][i]==a[1][i]==a[2][i]):
                        return a[i][i]
        if (a[0][0]==a[1][1]==a[2][2]) or (a[2][0]==a[1][1]==a[0][2]):
                        return a[1][1]

