"""


Create a function that returns the determinant of a given square matrix.

### Examples

    determinant([[3]]) ➞ 3
    
    determinant([[1, 0], [5, 4]]) ➞ 4
    
    determinant([[3, 0], [2, 2]]) ➞ 6
    
    determinant([[4, 8, 6], [2, 4, 3], [6, 2, 1]]) ➞ 0

### Notes

All inputs are square integer matrices.

"""

from functools import wraps
​
def memoize(fn):
  calls = []
  values = []
  @wraps(fn)
  def memoized(*args, **kwargs):
    if (args, kwargs) not in calls:
      values.append(fn(*args, **kwargs))
      calls.append((args, kwargs))
    return values[calls.index((args, kwargs))]
  return memoized
​
@memoize
def determinant(A):
  dim = len(A)
  if any(len(row)!=dim for row in A):
    raise TypeError("Not a square matrix")
  if dim==1:
    return A[0][0]
  det = 0
  for col in range(dim):
    det += (
      (1 if col%2==0 else -1)
      * A[0][col]
      * determinant([[row[i] for i in range(dim) if i!=col] for row in A[1:]])
    )
  return det

