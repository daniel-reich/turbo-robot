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
  A=[[],[]]
  for i in range(len(lst)):
    for j in range(len(lst)):
      if i==j:
        A[0].append(lst[i][j])
      if i+j+1==len(lst):
        A[1].append(lst[i][j])
  return A

