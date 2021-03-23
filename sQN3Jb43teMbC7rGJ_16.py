"""


In linear algebra, the transpose of a matrix is an operator which flips a
matrix over its diagonal; that is, it switches the row and column indices of
the _matrix A_ by producing another matrix, often denoted by _A^T_.

Create a function that takes a 2D matrix `m` and returns a 2D matrix (matrix
A^T).

### Examples

    makeTranspose([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
    ]
    
    makeTranspose([
      [1, 2],
      [3, 4],
      [5, 6]
    ]) ➞ [
      [1, 3, 5],
      [2, 4, 6]
    ]
    
    makeTranspose([
      ["a", "b"]
    ]) ➞ [
      ["a"],
      ["b"]
    ]

### Notes

N/A

"""

make_transpose = lambda m: [list(i) for i in zip(*m)]

