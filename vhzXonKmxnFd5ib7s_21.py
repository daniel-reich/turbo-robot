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

class Matrix:
  
  def __init__(self, matrix):
    self.mtx = matrix
    
    self.cols = []
    
    for c in range(len(self.mtx[0])):
      col = [self.mtx[r][c] for r in range(len(self.mtx))]
      self.cols.append(col)
  
  def multiply(self, other):
    
    if len(self.cols) != len(other.mtx):
      return 'invalid'
    
    nm = []
    
    for n in range(len(self.mtx)):
      sr = self.mtx[n]
      row = []
      for c in range(len(other.cols)):
        oc = other.cols[c]
        #print(sr, oc, len(sr), len(oc))
        products = [sr[i] * oc[i] for i in range(len(sr))]
        row.append(sum(products))
      nm.append(row)
    
    return Matrix(nm)
  
  def display(self):
    return self.mtx
      
      
      
def matrix_multiply(a, b):
  
  m1 = Matrix(a)
  m2 = Matrix(b)
  
  m3 = m1.multiply(m2)
  #print(m3)
  try:
    return m3.display()
  except AttributeError:
    return m3

