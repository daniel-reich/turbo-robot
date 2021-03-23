"""


Create a function that takes in **size** and **direction** and generates a
**diagonal rug**.

The size is the `n` parameter, and all rugs are square `n x n`. The direction
is whether the diagonal part begins on the left or the right side.

### Examples

    generate_rug(4, "left") ➞ [
      [0, 1, 2, 3],
      [1, 0, 1, 2],
      [2, 1, 0, 1],
      [3, 2, 1, 0]
    ]
    
    generate_rug(5, "right") ➞ [
      [4, 3, 2, 1, 0],
      [3, 2, 1, 0, 1],
      [2, 1, 0, 1, 2],
      [1, 0, 1, 2, 3],
      [0, 1, 2, 3, 4]
    ]
    
    generate_rug(1, "left") ➞ [
      [0]
    ]
    
    generate_rug(2, "right") ➞ [
      [1, 0],
      [0, 1]
    ]

### Notes

  * `n > 0`
  * A `1 x 1` rug is trivially `[[0]]` (same for left and right).

"""

def generate_rug(n, direction):
  dict = {"left": 1, "right": 0}
  lst, x = [], 0
  d = dict.get(direction)
  l = (1 if d else 0)
  r = (0 if d else 1)
  for i in range(0, n):
    f = x*l + (n-x-1)*r
    s = (x+1)*r + (n-x)*l
    lst.append([i for i in range(f, 0, -1)] + [i for i in range(0, s)])
    x += 1
  return lst

