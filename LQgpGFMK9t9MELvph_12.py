"""


Given a square list ( _n_ * _n_ size) implement a function that returns a new
list containing two lists equal to the two diagonals, in the following order:

    diagonal 1 = from upper-left to lower-right corner
    diagonal 2 = from upper-right to lower-left corner

### Examples

    get_diagonals([ [1, 2], [3, 4] ]) ➞ [ [1, 4], [2, 3] ]
    
    get_diagonals([ ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"] ]) ➞ [ ["a", "e", "i"], ["c", "e", "g"] ]
    
    get_diagonals([ [True] ]) ➞ [ [True], [True] ]

### Notes

  * Your function must also work with single elements or empty lists.
  * Try to build both diagonals with a single loop.

"""

def get_diagonals(lst):
  diag1 = []
  diag2 = []
  n = len(lst)
  i = 0
  while i < n:
    print(i, lst[i][i])
    diag1.append(lst[i][i])
    print(":",i, lst[i][n-i-1])
    diag2.append(lst[i][n-i-1])
    i = i+1
  return ([diag1, diag2])

