"""


Create a function that takes the **width** , **height** and **character** and
returns a picture frame as a 2D list.

### Examples

    get_frame(4, 5, "#") ➞ [
      ["####"],
      ["#  #"],
      ["#  #"],
      ["#  #"],
      ["####"]
    ]
    # Frame is 4 characters wide and 5 characters tall.
    get_frame(10, 3, "*") ➞ [
      ["**********"],
      ["*        *"],
      ["**********"]
    ]
    # Frame is 10 characters and wide and 3 characters tall.
    get_frame(2, 5, "0") ➞ "invalid"
    # Frame's width is not more than 2.

### Notes

  * Remember the gap.
  * Return `"invalid"` if **width** or **height** is _2 or less_ (can't put anything inside).

"""

import numpy as np
​
​
def get_frame(w, h, ch):
  if w < 3 or h < 3: return 'invalid'
  frame = np.array([
    [0 for _ in range(w)]
    for _ in range(h)
  ])
  frame[1:-1, 1:-1] += 1
  result = []
  for row in frame:
    new = [''.join(ch if i == 0 else ' ' for i in row)]
    result.append(new)
  return result

