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

class Matrix:
  class Space:
​
    def __init__(self, val, row, col):
      self.v = val
      self.r = row
      self.c = col
​
  def __init__(self, mtx):
    self.mtx = mtx
​
    self.spaces = {}
    self.rows = {}
    self.cols = {}
​
    for r in range(len(mtx)):
      row = []
      for c in range(len(mtx[0])):
        space = Matrix.Space(mtx[r][c], r, c)
        self.spaces['{},{}'.format(r,c)] = space
        row.append(space)
        if c in self.cols.keys():
          self.cols[c].append(space)
        else:
          self.cols[c] = [space]
      self.rows[r] = row
  
  def transpose(self):
    nm = []
    
    if len(self.mtx) == len(self.mtx[0]):
      for r in range(len(self.mtx)):
        row = []
        for c in range(len(self.mtx[0])):
          row.append(self.spaces['{},{}'.format(c, r)].v)
        nm.append(row)
    else:
      for c in range(len(self.mtx[0])):
        row = []
        for r in range(len(self.mtx)):
          row.append(self.spaces['{},{}'.format(r, c)].v)
        nm.append(row)
​
    return Matrix(nm)
​
  def multiply(self, other):
    
    if max(self.cols.keys()) != max(other.rows.keys()):
      return 'ERROR'
    
    nm = []
​
    for r in sorted(list(self.rows.keys())):
      row = []
      for c in sorted(list(other.cols.keys())):
        products = [self.rows[r][n].v * other.cols[c][n].v for n in range(len(self.rows[r]))]
        row.append(sum(products))
      nm.append(row)
    
    return Matrix(nm)
​
​
def multiply_matrix(m1, m2):
​
  m1 = Matrix(m1)
  m2 = Matrix(m2)
​
  product = m1.multiply(m2)
​
  if isinstance(product, str) == True:
    return product
  else:
    return product.mtx

