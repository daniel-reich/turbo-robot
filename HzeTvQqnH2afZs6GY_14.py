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

def generateRug(n, direction):
  temp = []
  result = []
  if direction == 'left':
    for i in range(n):
      temp.append(i)
    for i in range(n):
      a = i
      t = []
      b = -1
      for j in range(n):
        t.append(temp[a])
        if a == 0:
          b = 1
        a += b
      result.append(t)
    return result
  else:
    for i in range(n-1,-1,-1):
      temp.append(i)
    for i in range(n):
      a = i
      t = []
      b = 1
      for j in range(n):
        t.append(temp[a])
        if a == n-1:
          b = -1
        a += b
      result.append(t)
    return result

