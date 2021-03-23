"""


This challenge concerns _square matrices_ (same number of rows and columns) as
the below example illustrates:

    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]

The entries in the diagonal line from the top left to the bottom right form
the _main diagonal_ of the matrix. In this case, 1,5,9 form the main diagonal.

Write a function that returns the matrix obtained by replacing the entries
_above_ the main diagonal with 0s.

For example, for the matrix above you should return:

    [
      [1, 0, 0],
      [4, 5, 0],
      [7, 8, 9]
    ]

### Examples

    lower_triang([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [1, 0, 0],
      [4, 5, 0],
      [7, 8, 9]
    ]
    
    lower_triang([
      [5, 7],
      [7, 9]
    ]) ➞ [
      [5, 0],
      [7, 9]
    ]
    
    lower_triang([
      [1, 8, 8, 1],
      [2, 7, 7, 2],
      [3, 6, 6, 3],
      [4, 5, 5, 4]
    ]) ➞ [
      [1, 0, 0, 0],
      [2, 7, 0, 0],
      [3, 6, 6, 0],
      [4, 5, 5, 4]
    ]

### Notes

  * As in the examples, the size of the matrices will vary (but they will always be square).
  * In Linear Algebra, matrices with 0s above the diagonal are called _lower triangular matrices_.

"""

def lower_triang(arr):
    for i, sublist in enumerate(arr):
        sublist[i+1:]=[0]* len(sublist[i+1:])
        
    return arr

