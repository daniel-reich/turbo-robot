"""


Given a grid of numbers, return a grid of the **Spotlight Sum** of each
number. The spotlight sum can be defined as the total of all numbers
immediately surrounding the number on the grid, including the number in the
total.

### Examples

    spotlight_map([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [12, 21, 16],
      [27, 45, 33],
      [24, 39, 28]
    ]
    spotlight_map([
      [2, 6, 1, 3, 7],
      [8, 5, 9, 4, 0]
    ]) ➞ [
      [21, 31, 28, 24, 14],
      [21, 31, 28, 24, 14]
    ]
    spotlightMap([[3]]) ➞ [[3]]

### Notes

  * Note that all numbers have a spotlight sum, including numbers on the edges.
  * All inputs will be valid grid (all rows will have the same length).

"""

def spotlight_map(grid):
  def in_spot(a, k, d):
    return ((a==0 and (a==k or a==k+1)) or
      (a==len(d)-1 and (a==k or a==k-1)) or (a==k or a==k-1 or a==k+1))
​
  def get_sum(x, y):
    return sum([sum([row[j] for j, col in enumerate(row) if
      in_spot(x, i, row) and in_spot(y, j, grid)])
        for i, row in enumerate(grid)])
​
  return [[get_sum(i, j) for j, col in enumerate(row)] for i, row in enumerate(grid)]

