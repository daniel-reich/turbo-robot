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
  trb=[list(x) for x in zip(*b)]
  if len(a[0])==len(b):
    res=[[0 for j in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(res)):
      for j in range(len(res[0])):
        res[i][j]=sum(a[i][k]*trb[j][k] for k in range(len(a[0])))
    return res      
  else:
    return "invalid"

