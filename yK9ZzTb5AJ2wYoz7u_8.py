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

def floyd(up_to = None, n_row = None):
  newlist = []
  newlist2 = []
  counter = 1
  count_rows = 0
  amount_per_row = 1
  if up_to == None:
    while count_rows < n_row:
      for i in range(amount_per_row):
        newlist2.append(counter)
        counter += 1
      newlist.append(newlist2)
      amount_per_row += 1
      count_rows += 1
      newlist2 = []
    return newlist
  else:
    while up_to not in newlist2:
      for i in range(amount_per_row):
        newlist2.append(counter)
        counter += 1
      newlist.append(newlist2)
      amount_per_row += 1
      if up_to in newlist2:
        return newlist
      else:
        newlist2 = []
    print(newlist)

