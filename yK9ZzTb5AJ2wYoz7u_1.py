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

from math import ceil,sqrt
def floyd(up_to = None, n_row = None):
  lst = []
  if up_to:
    n_row = ceil((-1 + sqrt(1+8*up_to))/2)
  start = lambda x: (x+1) * x // 2
  for i in range(1,n_row+1):
    lst.append(list(range(start(i-1)+1,start(i-1)+i+1)))
  return lst

