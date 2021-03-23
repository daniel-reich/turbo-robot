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
    if up_to != None:
        rows = 1
        while rows * (rows + 1) // 2 < up_to:
            rows += 1
    else:
        rows = n_row
    ans = []
    start = 1
    for row in range(1, rows + 1):
        ans.append(list(range(start, start + row)))
        start += row
    return ans

