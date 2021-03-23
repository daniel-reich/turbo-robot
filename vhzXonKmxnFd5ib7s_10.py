"""


Create a function that multiplies two matrices (n x m) and (p x q) and
returns:

  * `"invalid"` if the matrices are not multiplicable (i.e. if m is not equal to p).
  * The multiplication matrix (n x q) otherwise.

### Examples

    matrix_multiply([[1, 2]], [[3], [4]]) ➞ [[11]]
    
    matrix_multiply([[0, 0], [0, 1]], [[1, 2], [3, 4], [5, 6]]) ➞ "invalid"
    
    matrix_multiply([[4, 2], [3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]

### Notes

This challenge is a generalized version of [Matrix
Multiplication](https://edabit.com/challenge/dfep4NR2twAFTdt9k).

"""

def matrix_multiply(a, b):
  rowA = len(a)
  rowB = len(b)
  colA = len(a[0])
  colB = len(b[0])
​
  if colA != rowB:
    return "invalid"
​
  result = []
  for i in range(rowA):
    row = []
    for j in range(colB):
      value = 0
      for k in range(colA):
        value += a[i][k] * b[k][j]
      row.append(value)
    result.append(row)
​
  return result

