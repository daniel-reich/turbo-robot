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
    touch_lr = all([sublist[0]==0 and sublist[-1]==0 for sublist in lst])
    touch_ud = 1 not in lst[0] and 1 not in lst[-1]
    return touch_lr and touch_ud

