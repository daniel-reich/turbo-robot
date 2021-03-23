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
  import numpy as np
​
  if n==1:
    return [[0]]
    
  num=int((n-1)/2)
  Y=np.zeros((n,n))
  Y[0:n:n-1,:]=num
  Y[:,0:n:n-1]=num
  Y[1:n-1,1:n-1]=generate_rug(n-2)
  
  return Y.tolist()

