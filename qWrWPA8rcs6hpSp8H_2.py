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

from itertools import permutations
from functools import reduce
def determinant(A):
  fact = [reduce(lambda a,b:a*b,range(1,i+2)) for i in range(len(A)-1) if i%2]
  return sum([reduce(lambda a,b:a*b,[A[i][i2] for i,i2 in enumerate(p)]) \
    * [1, -1][(sum([ip//f for f in fact])+ip)%2] for ip,p in enumerate(permutations(range(len(A))))])

