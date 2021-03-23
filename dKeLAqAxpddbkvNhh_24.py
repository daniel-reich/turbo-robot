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
​
  return sum(1 for x in lst for i in range(len(x)-(n-1)) if x[i:i+n] == [0] * n)

