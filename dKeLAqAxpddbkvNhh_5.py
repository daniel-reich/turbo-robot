"""


A group of `n` friends are going to see a movie. They would like to find a
spot where they can sit next to each other in the same row. A movie theater's
seat layout can be represented as a 2-D matrix, where `0`s represent empty
seats and `1`s represent taken seats.

    [[1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0]]

Create a function that, given a seat layout and the number of friends `n`,
returns the number of available spots for all `n` friends to sit together. In
the above example, if `n = 3`, there would be 2 spots (the first row and last
row).

### Examples

    group_seats([
      [1, 0, 1, 0, 1, 0, 1],
      [0, 1, 0, 1, 0, 1, 0],
      [0, 0, 1, 1, 1, 1, 1],
      [1, 0, 1, 1, 0, 0, 1],
      [1, 1, 1, 0, 1, 0, 1],
      [0, 1, 1, 1, 1, 0, 0]
    ], 2) ➞ 3
    
    group_seats([
      [1, 0, 1, 0, 1, 0, 1],
      [0, 1, 0, 0, 0, 0, 0],
    ], 4) ➞ 2

### Notes

Multiple free arrangements that overlap still count as distinct arrangements
(see example #2).

"""

def group_seats(lst, n):
  ctr = 0
  for i in range(len(lst)):
    for j in range(len(lst[i])-n+1):
      if sum(lst[i][j:j+n]) == 0:
        ctr += 1
  return ctr

