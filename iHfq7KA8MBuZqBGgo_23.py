"""


Suppose a swimming pool blueprint can be represented as a 2D list, where `1`s
represent the pool and `0`s represent the rest of the backyard.

    [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
    # Legitimate

Suppose a pool is considered **legitimate** if it does not touch any of the
four borders in this 2D list.

    [[1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
    # Illegitimate! 
    # The 1s are touching both the left "fence" and the upper "fence".

Create a function that returns `True` if the pool plan is legitimate, and
`False` otherwise.

### Examples

    is_legitimate([
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]) ➞ True
    
    is_legitimate([
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 0, 0],
      [0, 0, 1, 1, 1, 0, 0, 0]
    ]) ➞ False
    
    is_legitimate([
      [0, 0, 0, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 0, 0, 0]
    ]) ➞ True

### Notes

N/A

"""

def is_legitimate(lst):
  return sum(i[0] + i[-1] for i in lst) + sum(lst[0]) + sum(lst[-1]) < 1

