"""


Create a function that takes in the size of the line and the number of people
waiting and places people in an _S-shape_ ordering. The demonstration below
will make it clear:

    # Ordering numbers 1-15 in a [5,3] space.
    
    order_people([5, 3], 15) ➞ [
      [1, 2, 3],
      [6, 5, 4],
      [7, 8, 9],
      [12, 11, 10],
      [13, 14, 15]
    ]

If there is extra room, leave those spots blank with a `0` filler.

    # Ordering numbers 1-5 in a [4, 3] space.
    
    order_people([4, 3], 5) ➞ [
      [1, 2, 3],
      [0, 5, 4],
      [0, 0, 0],
      [0, 0, 0]
    ]

If there are too many people for the given dimensions, return `"overcrowded"`.

    order_people([4, 3], 20) ➞ "overcrowded"

### Examples

    order_people([3, 3], 8) ➞ [
      [1, 2, 3],
      [6, 5, 4],
      [7, 8, 0]
    ]
    
    order_people([2, 4], 5) ➞ [
      [1, 2, 3, 4],
      [0, 0, 0, 5]
    ]
    
    order_people([2, 4], 10) ➞ "overcrowded"

### Notes

  * Always start the ordering on the upper-left corner.
  * If the **S-shape** concept doesn't make sense, try writing down some of these examples on a piece of paper and tracing a pencil through the numbers in order.

"""

import numpy as np
def order_people(lst, people):
  if lst[0] * lst[1] >= people:
    a = np.arange(1, lst[0]*lst[1]+1).reshape(lst[0], lst[1])
    b = lst[0]*lst[1] - people
    row = b // lst[1]
    col = b % lst[1]
    if row != 0 and col != 0:
      a[-row-1, -col:] = a[-row:] = 0
    elif row != 0 and col == 0:
      a[-row:] = 0
    elif row == 0 and col != 0:
      a[-row-1, -col:] = 0
    for i in range(lst[0]):
      if i % 2 == 1:
        a[i] = a[i, ::-1]
    return a.tolist()
  else:
    return "overcrowded"

