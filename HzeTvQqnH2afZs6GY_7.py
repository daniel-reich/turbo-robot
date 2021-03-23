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

def generate_rug(a,d):
  lis=[]
  for i in range(a):
    lisa=[]
    while len(lisa)<a:
      lisa.append(0)
    lis.append(lisa)
  i=0
  while i<a:
    lisa=[i for i in range(a-i)]
    lisum=[i for i in range(i,len(lis))]
    for j,k in zip(lisum,lisa):
      lis[i][j]=k
      lis[j][i]=k
    i+=1
  if d=="left":
    return lis
  elif d=="right":
    return lis[::-1]

