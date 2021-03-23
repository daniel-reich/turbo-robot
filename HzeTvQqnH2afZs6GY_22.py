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
  rug=[n-1]*n
  for i in range(n):
    rug[i]=[rug[i]]*n
  if direction=='left':
    for i in range(n):
      rug[i][i]=0
  elif direction=='right':
    for i in range(n):
      rug[n-i-1][i]=0
  for i in range(n):
    for x in range(n):
      if rug[i][x]==0:
        for a in range(x+1,n):
          rug[i][a]=rug[i][a-1]+1
        for a in range(x-1,-1,-1):
          rug[i][a]=rug[i][a+1]+1
  for i in rug:
    print(i)
  return rug

