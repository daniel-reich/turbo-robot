"""


Create a function that takes a list representation of a Minesweeper board, and
returns another board where the value of each cell is the amount of its
neighbouring mines.

### Examples

The input may look like this:

    [
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 1, 0, 1],
      [1, 1, 0, 0]
    ]

The `0` represents an **empty space** . The `1` represents a **mine**.

You will have to replace each **mine** with a `9` and each **empty space**
with the number of adjacent mines, the output will look like this:

    [
      [1, 9, 2, 1],
      [2, 3, 9, 2],
      [3, 9, 4, 9],
      [9, 9, 3, 1]
    ]

### Notes

  * Since in the output the numbers `0-8` are used to determine the amount of adjacent mines, the number `9` will be used to identify the mines instead.
  * A wikipedia page explaining how Minesweeper works is available in the **Resources** tab.

"""

def minesweeper_numbers(lst):
  A=[[0 for j in range(len(lst[0]))] for i in range(len(lst))]
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      if lst[i][j]==1:
        A[i][j]=9
      else:
        A[i][j]=[lst[k][t] for k in range(len(lst)) for t in range(len(lst[0])) if abs(i-k)<2 and abs(j-t)<2].count(1)
  return A

