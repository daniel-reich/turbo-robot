"""


Your task, is to create `N x N` multiplication table, of size `n` provided in
parameter.

For example, when `n` is 5, the multiplication table is:

  * 1, 2, 3, 4, 5
  * 2, 4, 6, 8, 10
  * 3, 6, 9, 12, 15
  * 4, 8, 12, 16, 20
  * 5, 10, 15, 20, 25

This example will result in:

    [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

### Examples

    multiplication_table(1) ➞ [[1]]
    
    multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

### Notes

N/A

"""

class Multiplication_Table:
  class Row:
​
    def __init__(self, rval, size):
      self.rval = rval
      self.size = size
​
      self.row = [rval * n for n in range(1, size + 1)]
  
  def __init__(self, val):
    self.val = val
​
    self.rows = {n:Multiplication_Table.Row(n, val) for n in range(1, val+1)}
  
  def display(self):
    tr = []
    for n in sorted(self.rows.keys()):
      tr.append(self.rows[n].row)
    return tr
​
def multiplication_table(n):
  table = Multiplication_Table(n)
  return table.display()

