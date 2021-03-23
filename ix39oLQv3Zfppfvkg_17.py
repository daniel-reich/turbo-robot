"""


  1. The main condition of matrix multiplication is that the number of columns of the 1st matrix must equal to the number of rows of the 2nd one.
  2. As a result of multiplication you will get a new matrix that has the same quantity of rows as the 1st one has and the same quantity of columns as the 2nd one.
  3. For example if you multiply a matrix of "n" * "k" by "k" * "m" size you"ll get a new one of "n" * "m" dimensions.

Create a function that takes 2 x 2D lists `m1` and `m2` as arguments and
returns a 2D list (matrix C). C = A*B.

  * If the number of columns of the 1st matrix isn't equal to the number of rows of the 2nd: return `"ERROR"`.

### Examples

    multiply_matrix([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ], [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [30, 36, 42],
      [66, 81, 96],
      [102, 126, 150]
    ]

### Notes

N/A

"""

def multiply_matrix(m1, m2):
  if len(m1[0])!=len(m2): return "ERROR"
  return [[sum(a*b for a,b in zip(x,y)) for y in zip(*m2)] for x in m1]

