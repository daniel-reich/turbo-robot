"""


Floyd's triangle is a right-angled triangular array of natural numbers. It's
defined by filling the rows of the triangle with consecutive numbers, starting
with a 1 in the top left corner:

![Floyd's triangle](https://edabit-challenges.s3.amazonaws.com/CTyQyko_d.webp)

Write a function that takes an integer `n` and returns Floyd's triangle's rows
as a list of lists. Your function should return one of two possibilities:

  * If a value is passed to `n_row`, return the first `n` rows.
  * If a value is passed to `up_to`, return all rows up to, and including, the row that contains `n`.

Expect an argument to be passed to one parameter or the other, but not both.

### Examples

    floyd(up_to = 5) ➞ [[1], [2, 3], [4, 5, 6]]
    # The third row contains a 5.
    
    floyd(n_row = 5) ➞[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
    # Returns the first five rows.
    
    floyd(up_to = 10) ➞ [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
    
    floyd(n_row = 1) ➞[[1]]

### Notes

Hint: You can define `n_row` from `up_to` using the triangular number
sequence. That is, `n_row` should be x in the equation (x*(x+1))/2 = `up_to`
rounded up. Then, you only need to write a function for `n_row`.

"""

class Triangle:
  
  def __init__(self, triangle = []):
    self.tri = triangle
    self.last_num = 0
    self.next_row_size = 1
  
  def add_row(self):
    row = []
    while len(row) < self.next_row_size:
      row.append(self.last_num + 1)
      self.last_num += 1
    self.tri.append(row)
    self.next_row_size += 1
    return True
  
  def up_to(self, goal):
    tr = []
    
    for row in self.tri:
      tr.append(row)
      if goal in row:
        break
    
    return tr
  
  def n_row(self, row):
    return self.tri[:row]
  
  def increase_to(self, size):
    while len(self.tri) < size:
      self.add_row()
    return True
​
floyd_triangle = Triangle()
​
floyd_triangle.increase_to(11)
​
def floyd(up_to = None, n_row = None):
  if up_to == None:
    return floyd_triangle.n_row(n_row)
  else:
    return floyd_triangle.up_to(up_to)

