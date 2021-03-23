"""


Create a function that takes in parameter `n` and generates an `n x n` (where
`n` is odd) **concentric rug**.

The center of a concentric rug is `0`, and the rug "fans-out", as show in the
examples below.

### Examples

    generate_rug(1) ➞ [
      [0]
    ]
    
    generate_rug(3) ➞ [
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]
    ]
    
    generate_rug(5) ➞ [
      [2, 2, 2, 2, 2],
      [2, 1, 1, 1, 2],
      [2, 1, 0, 1, 2],
      [2, 1, 1, 1, 2],
      [2, 2, 2, 2, 2]
    ]
    
    generate_rug(7) ➞ [
      [3, 3, 3, 3, 3, 3, 3],
      [3, 2, 2, 2, 2, 2, 3],
      [3, 2, 1, 1, 1, 2, 3],
      [3, 2, 1, 0, 1, 2, 3],
      [3, 2, 1, 1, 1, 2, 3],
      [3, 2, 2, 2, 2, 2, 3],
      [3, 3, 3, 3, 3, 3, 3]
    ]

### Notes

  * `n >= 0`.
  * Always increment by 1 each "layer" outwards you travel.

"""

def generate_rug(n):
  if (n % 2) == 0 :
    return False
  if n == 1:
    return [[0]]
  elif n == 3 :
    return [[1,1,1],[1,0,1],[1,1,1]]
  else:
    mxv = n // 2
    answer = [[0 for x in range(n)] for y in range(n)]
    print(answer)
    for i in range(mxv+1):
      for j in range(mxv+1):
        cellval = max(abs(i-mxv),abs(j-mxv))
        answer[i][j] = cellval
        answer[-(i+1)][j] = cellval
        answer[-(i+1)][-(j+1)] = cellval
        answer[i][-(j+1)] = cellval
    answer[mxv][mxv] = 0
    return answer

